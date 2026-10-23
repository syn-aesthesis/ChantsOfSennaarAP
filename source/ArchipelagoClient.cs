using System;
using System.Linq;
using System.Threading;
using System.Collections.Generic;
using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.BounceFeatures.DeathLink;
using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.Helpers;
using Archipelago.MultiClient.Net.MessageLog.Messages;
using Archipelago.MultiClient.Net.Packets;

namespace ChantsOfSennaarAP;

// based on ArchipelagoBepInExPluginTemplate https://github.com/alwaysintreble/ArchipelagoBepInExPluginTemplate/
public class ArchipelagoClient {
    public const string APVersion = "0.6.7";
    private const string Game = "Chants of Sennaar";

    public static bool Authenticated;
    private bool _attemptingConnection;

    public static ArchipelagoData ServerData = new();
    private static DeathLinkHandler _deathLinkHandler;
    private static ArchipelagoSession _session;

    public static readonly HashSet<string> ChecksSentThisSession = new HashSet<string>();
    public static readonly Queue<string> ChecksPending = new Queue<string>();
    public static readonly Queue<string> ItemsPending = new Queue<string>();

    private long _goalType;


    // Call to connect to an Archipelago session (connection info should already be set up on ServerData)
    public void Connect() {
        if (Authenticated || _attemptingConnection)
            return;

        try {
            _session = ArchipelagoSessionFactory.CreateSession(ServerData.Server);
            SetupSession();
        }
        catch (Exception e) {
            Plugin.Logger.LogError(e);
        }

        TryConnect();
    }

    // Add handlers for Archipelago events
    private void SetupSession() {
        _session.MessageLog.OnMessageReceived += message => ArchipelagoConsole.LogMessage(message.ToString());
        _session.Items.ItemReceived += OnItemReceived;
        _session.Socket.PacketReceived += OnSessionPacketReceived;
        _session.Socket.ErrorReceived += OnSessionErrorReceived;
        _session.Socket.SocketClosed += OnSessionSocketClosed;

        FlushChecks(); // send any checks queued while offline
    }

    // Attempt to connect to the server with our connection info
    private void TryConnect() {
        try {
            ThreadPool.QueueUserWorkItem(_ =>
                HandleConnectResult(
                    _session.TryConnectAndLogin(
                        Game,
                        ServerData.Slot,
                        ItemsHandlingFlags.AllItems,
                        new Version(APVersion),
                        password: ServerData.Password,
                        requestSlotData: ServerData.NeedSlotData
                    )
                )
            );
        }
        catch (Exception e) {
            Plugin.Logger.LogError(e);
            HandleConnectResult(new LoginFailure(e.ToString()));
            _attemptingConnection = false;
        }
    }

    // Handle result (success/failure) of connection attempt
    private void HandleConnectResult(LoginResult result) {
        string outText;
        if (result.Successful) {
            var success = (LoginSuccessful)result;

            ServerData.SetupSession(success.SlotData, _session.RoomState.Seed);
            Authenticated = true;

            _deathLinkHandler = new(_session.CreateDeathLinkService(), ServerData.Slot);
            _session.Locations.CompleteLocationChecksAsync(ServerData.CheckedLocations.ToArray());
            outText = $"Successfully connected to {ServerData.Server} as {ServerData.Slot}!";
            ArchipelagoConsole.LogMessage(outText);
        }
        else {
            var failure = (LoginFailure)result;
            outText = $"Failed to connect to {ServerData.Server} as {ServerData.Slot}";
            outText = failure.Errors.Aggregate(outText, (current, error) => current + $"\n    {error}");

            Plugin.Logger.LogError(failure);
            Authenticated = false;
            Disconnect();
        }

        ArchipelagoConsole.LogMessage(outText);
        _attemptingConnection = false;
    }

    // Disconnect from the server, clean up and re-null session
    private void Disconnect() {
        Plugin.Logger.LogDebug("Disconnecting from server...");
        _session?.Socket.DisconnectAsync();
        _session = null;
        Authenticated = false;
    }

    public void SendMessage(string message) {
        _session.Socket.SendPacketAsync(new SayPacket { Text = message });
    }

    // Handle packets to parse slot YAML options
    private void OnSessionPacketReceived(ArchipelagoPacketBase packet) {
        if (packet is ConnectedPacket connectedPacket) {
            Plugin.Logger.LogDebug($"Packet received: {connectedPacket}");

            if (connectedPacket.SlotData.TryGetValue("goal_type", out object goalOption)) {
                _goalType = (long)goalOption;
            }
        }
    }

    // Handle socket connection errors
    private void OnSessionErrorReceived(Exception e, string message) {
        Plugin.Logger.LogError(e);
        ArchipelagoConsole.LogMessage(message);
    }

    // Handle socket closures
    private void OnSessionSocketClosed(string reason) {
        Plugin.Logger.LogError($"Connection to Archipelago lost: {reason}");
        Disconnect();
    }


    // Enqueue items received by slot for granting in-game
    private void OnItemReceived(ReceivedItemsHelper helper) {
        var receivedItem = helper.DequeueItem();
        if (helper.Index <= ServerData.Index)
            return;
        ServerData.Index++;

        ItemsPending.Enqueue(receivedItem.ItemName);
        Plugin.Logger.LogDebug($"Item enqueued for receiving: {receivedItem.ItemName}");
    }

    // Handle enqueued items; called from Update() in main thread
    public static bool TryGetReceivedItem(out string itemName) {
        if (ItemsPending.Count > 0) {
            itemName = ItemsPending.Dequeue();
            return true;
        }

        itemName = null;
        return false;
    }

    // Enqueue current check for sending; called from Harmony patches
    public static void SendCheck(string locationName) {
        if (!_session.Socket.Connected)
            return;
        if (!ChecksSentThisSession.Add(locationName))
            return;

        ChecksPending.Enqueue(locationName);
        Plugin.Logger.LogDebug($"Check enqueued for sending: {locationName}");

        FlushChecks();
    }

    // Send all enqueued checks if connected; call on connect and after each SendCheck()
    private static void FlushChecks() {
        if (!_session.Socket.Connected)
            return;

        var locationIds = new List<long>();
        while (ChecksPending.Count > 0) {
            string locationName = ChecksPending.Dequeue();
            long locationId = _session.Locations.GetLocationIdFromName(Game, locationName);

            if (locationId == -1) {
                Plugin.Logger.LogWarning($"Unknown location name: {locationName}");
                continue;
            }

            if (_session.Locations.AllLocationsChecked.Contains(locationId))
                continue;

            locationIds.Add(locationId);
        }

        if (locationIds.Count > 0) {
            _session.Locations.CompleteLocationChecks(locationIds.ToArray());
            Plugin.Logger.LogDebug($"Checks sent: {string.Join(", ", locationIds)}");
        }
    }

    // Sends goal packet; called from Harmony patches
    public static void SendGoalPacket() {
        if (!_session.Socket.Connected)
            return;
        
        var goalPacket = new StatusUpdatePacket {
            Status = ArchipelagoClientState.ClientGoal
        };
        _session.Socket.SendPacketAsync(goalPacket);
    }

}