using BepInEx;
using BepInEx.Logging;
using HarmonyLib;
using UnityEngine;
using UnityEngine.SceneManagement;
using System;
using System.Collections.Generic;
using Archipelago.MultiClient.Net.Models;

namespace ChantsOfSennaarAP;

[BepInPlugin(PluginGuid, PluginName, PluginVersion)]
public class Plugin : BaseUnityPlugin {
    private const string PluginGuid = "gg.archipelago.chantsofsennaar";
    public const string PluginName = "ChantsOfSennaarAP";
    private const string PluginVersion = "0.1.1";

    public const string ModDisplayInfo = $"{PluginName} v{PluginVersion}";
    private const string APDisplayInfo = $"Archipelago v{ArchipelagoClient.APVersion}";
    
    public new static ManualLogSource Logger;
    public static ArchipelagoClient APClient;
    private readonly Harmony _harmony = new Harmony(PluginGuid);

    public static bool SplashFinished = false;
    private static readonly Dictionary<string, LanguageType> languageTypes = new() {
        { "Devotee", LanguageType.DEVOTS },
        { "Warrior", LanguageType.GUERRIERS },
        { "Bard", LanguageType.BARDES },
        { "Alchemist", LanguageType.ALCHIMISTES },
        { "Anchorite", LanguageType.RECLUS },
    };
    
    private void Awake() {
        Logger = base.Logger;
        APClient = new ArchipelagoClient();
        ArchipelagoConsole.Awake();

        SceneManager.sceneLoaded += OnSceneLoaded;
        
        this._harmony.PatchAll();
    }

    private void OnSceneLoaded(Scene scene, LoadSceneMode mode)
    {
        Logger.LogInfo($"Scene loaded: {scene.name}");
    }

    private void OnGUI() {
        if (!SplashFinished)
            return;
        
        // show in the corner that the mod is currently loaded
        GUI.Label(new Rect(16, 16, 300, 20), ModDisplayInfo);
        ArchipelagoConsole.OnGUI();

        // show the Archipelago version and whether we're connected or not
        string statusMessage;
        if (ArchipelagoClient.Authenticated) {
            // if your game doesn't usually show the cursor this line may be necessary
            // Cursor.visible = false;

            statusMessage = " Status: Connected";
            GUI.Label(new Rect(16, 40, 300, 20), APDisplayInfo + statusMessage);
        }
        else {
            // if your game doesn't usually show the cursor this line may be necessary
            // Cursor.visible = false;
            
            statusMessage = " Status: Disconnected";
            GUI.Label(new Rect(16, 40, 300, 20), APDisplayInfo + statusMessage);
            GUI.Label(new Rect(16, 60, 150, 20), "Host: ");
            GUI.Label(new Rect(16, 80, 150, 20), "Player Name: ");
            GUI.Label(new Rect(16, 100, 150, 20), "Password: ");
            
            ArchipelagoClient.ServerData.Server = GUI.TextField(new Rect(150, 60, 150, 20),
                ArchipelagoClient.ServerData.Server);
            ArchipelagoClient.ServerData.Slot = GUI.TextField(new Rect(150, 80, 150, 20),
                ArchipelagoClient.ServerData.Slot);
            ArchipelagoClient.ServerData.Password = GUI.TextField(new Rect(150, 100, 150, 20),
                ArchipelagoClient.ServerData.Password);
            
            // requires the player to enter a slot name
            if (GUI.Button(new Rect(16, 120, 100, 20), "Connect") &&
                !ArchipelagoClient.ServerData.Slot.IsNullOrWhiteSpace())
            {
                APClient.Connect();
            }
        }
        
        // this is a good place to create and add a bunch of debug buttons
    }

    void Update() {
        ArchipelagoClient.ApplyPendingItems(GrantItem);
    }

    // Returns true when handled, false to retry next frame
    private bool GrantItem(ItemInfo item) {
        var parts = item.ItemName.Split(' ');
        
        // Handle runes
        if (parts.Length == 3) {
            if (parts[1] == "Rune") {
                if (!languageTypes.TryGetValue(parts[0], out var lang) || 
                    !int.TryParse(parts[2], out var runeNum)) {
                    Logger.LogWarning($"Unrecognised rune item: {item.ItemName}");
                    return true;
                }

                try {
                    GameController.GetInstance().GetLanguageController().GetLanguageData(lang)
                        .AddRuneIfUnknown(runeNum - 1);
                    return true;
                }
                catch (Exception e) {
                    Logger.LogWarning($"Couldn't grant {item.ItemName} yet: {e.Message}");
                    return false;
                }
            }
        }

        // All other items
        return true;
    }
}
