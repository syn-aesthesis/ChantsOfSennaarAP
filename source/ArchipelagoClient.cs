using System;
using System.Linq;
using System.Threading;
using System.Collections.Concurrent;
using System.Collections.Generic;
using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.BounceFeatures.DeathLink;
using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.Helpers;
using Archipelago.MultiClient.Net.MessageLog.Messages;
using Archipelago.MultiClient.Net.Models;
using Archipelago.MultiClient.Net.Packets;

namespace ChantsOfSennaarAP;

// based on ArchipelagoBepInExPluginTemplate https://github.com/alwaysintreble/ArchipelagoBepInExPluginTemplate/
public class ArchipelagoClient {
    public const string APVersion = "0.6.7";
    private const string Game = "Chants of Sennaar";

    public static bool Authenticated;
    public volatile bool ItemsDirty;
    private bool _attemptingConnection;

    public static ArchipelagoData ServerData = new();
    private static DeathLinkHandler _deathLinkHandler;
    private static ArchipelagoSession _session;
    
    public static ArchipelagoSave SaveData;
    private static int _itemsApplied;

    public static readonly HashSet<string> ChecksSentThisSession = new HashSet<string>();
    public static readonly Queue<string> ChecksPending = new Queue<string>();

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
            outText = $"Successfully connected to {ServerData.Server} as {ServerData.Slot}!";
            ArchipelagoConsole.LogMessage(outText);

            ServerData.SetupSession(success.SlotData, _session.RoomState.Seed);
            SaveData = ArchipelagoSave.LoadOrCreate(_session.RoomState.Seed, ServerData.Slot, success.Team);

            foreach (var name in ChecksPending)
                SaveData.AddCheck(name);
            foreach (var name in SaveData.SnapshotChecks())
                ChecksPending.Enqueue(name);
            SaveData.Save();
            
            _itemsApplied = 0;
            Authenticated = true;

            _deathLinkHandler = new(_session.CreateDeathLinkService(), ServerData.Slot);
            FlushChecks();
            if (SaveData.GoalReached)
                TrySendGoal();
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

    public static void ApplyPendingItems(Func<ItemInfo, bool> tryGrant) {
        var session = _session;
        if (!Authenticated || session == null)
            return;

        var all = session.Items.AllItemsReceived.ToList();
        int count = all.Count;

        if (count < _itemsApplied)
            _itemsApplied = 0;

        while (_itemsApplied < count) {
            if (!tryGrant(all[_itemsApplied]))
                break;
            _itemsApplied++;
        }
    }

    public static void ResetItemsApplied() => _itemsApplied = 0;

    // Enqueue current check for sending; called from Harmony patches
    public static void SendCheck(string locationName) {
        if (!ChecksSentThisSession.Add(locationName))
            return;
        
        if (SaveData != null && SaveData.AddCheck(locationName))
            SaveData.Save();

        ChecksPending.Enqueue(locationName);
        Plugin.Logger.LogDebug($"Check enqueued for sending: {locationName}");
        FlushChecks();
    }

    // Send all enqueued checks if connected; call on connect and after each SendCheck()
    private static void FlushChecks() {
        var session = _session;
        if (!Authenticated || session?.Socket?.Connected != true)
            return;

        var ids = new HashSet<long>();
        while (ChecksPending.TryDequeue(out var name)) {
            long id = _session.Locations.GetLocationIdFromName(Game, name);
            if (id == -1) {
                Plugin.Logger.LogWarning($"Unknown location name: {name}");
                continue;
            }
            if (_session.Locations.AllLocationsChecked.Contains(id))
                continue;
            ids.Add(id);
        }

        if (ids.Count > 0) {
            _session.Locations.CompleteLocationChecks(ids.ToArray());
            Plugin.Logger.LogDebug($"Checks sent: {string.Join(", ", ids)}");
        }
    }

    // Sends goal packet; called from Harmony patches
    public static void SendGoalPacket() {
        if (SaveData != null) {
            SaveData.GoalReached = true;
            SaveData.Save();
        }
        TrySendGoal();
    }

    private static void TrySendGoal() {
        var session = _session;
        if (!Authenticated || session.Socket.Connected != true)
            return;
        _session.Socket.SendPacketAsync(new StatusUpdatePacket {
            Status = ArchipelagoClientState.ClientGoal
        });
    }

}