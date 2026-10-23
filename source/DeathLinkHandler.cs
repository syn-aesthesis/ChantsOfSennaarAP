using System;
using System.Collections.Generic;
using Archipelago.MultiClient.Net.BounceFeatures.DeathLink;
using BepInEx;

namespace ChantsOfSennaarAP;

// based on ArchipelagoBepInExPluginTemplate https://github.com/alwaysintreble/ArchipelagoBepInExPluginTemplate/
public class DeathLinkHandler {
    private static bool _deathLinkEnabled;
    private readonly string _slotName;
    private readonly DeathLinkService _service;
    private readonly Queue<DeathLink> _deathLinks = new();

    // Instantiates handler, sets up hook for receiving death links, enables death link when specified
    public DeathLinkHandler(DeathLinkService deathLinkService, string name, bool enableDeathLink = false) {
        _service = deathLinkService;
        _service.OnDeathLinkReceived += DeathLinkReceived;
        _slotName = name;
        _deathLinkEnabled = enableDeathLink;

        if (_deathLinkEnabled) {
            _service.EnableDeathLink();
        }
    }

    public void ToggleDeathLink() {
        _deathLinkEnabled = !_deathLinkEnabled;

        if (_deathLinkEnabled) {
            _service.EnableDeathLink();
        }
        else {
            _service.DisableDeathLink();
        }
    }

    // Specifies behavior upon receiving a death link
    private void DeathLinkReceived(DeathLink deathLink) {
        _deathLinks.Enqueue(deathLink);
        Plugin.Logger.LogDebug(deathLink.Cause.IsNullOrWhiteSpace()
            ? $"Received death link from: {deathLink.Source}"
            : deathLink.Cause
        );
    }

    // Can be called when in a valid state to kill the player
    // If a death link is in the queue, dequeues death link and immediately kills the player
    public void KillPlayer() {
        try {
            if (_deathLinks.Count < 1)
                return;

            var deathLink = _deathLinks.Dequeue();
            var cause = deathLink.Cause.IsNullOrWhiteSpace() ? GetDeathLinkCause(deathLink) : deathLink.Cause;

            // TODO: kill the player
            Plugin.Logger.LogMessage(cause);
        }
        catch (Exception e) {
            Plugin.Logger.LogError(e);
        }
    }

    // Returns message for the player to see when a death link is received without a cause
    private string GetDeathLinkCause(DeathLink deathLink) {
        return $"Received death from {deathLink.Source}";
    }

    // Called to send a death link to the multiworld
    public void SendDeathLink() {
        try {
            if (!_deathLinkEnabled)
                return;

            Plugin.Logger.LogMessage("Sharing your death...");

            // TODO: Add cause here
            var linkToSend = new DeathLink(_slotName);
            _service.SendDeathLink(linkToSend);
        }
        catch (Exception e) {
            Plugin.Logger.LogError(e);
        }
    }
}