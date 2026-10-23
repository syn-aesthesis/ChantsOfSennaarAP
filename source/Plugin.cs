using BepInEx;
using BepInEx.Logging;
using HarmonyLib;
using UnityEngine;
using UnityEngine.SceneManagement;
using System.Collections.Generic;

namespace ChantsOfSennaarAP;

[BepInPlugin(PluginGuid, PluginName, PluginVersion)]
public class Plugin : BaseUnityPlugin {
    private const string PluginGuid = "gg.archipelago.chantsofsennaar";
    private const string PluginName = "ChantsOfSennaarAP";
    private const string PluginVersion = "0.1.0";

    private const string ModDisplayInfo = $"{PluginName} v{PluginVersion}";
    private const string APDisplayInfo = $"Archipelago v{ArchipelagoClient.APVersion}";
    
    public new static ManualLogSource Logger;
    public static ArchipelagoClient APClient;
    private readonly Harmony _harmony = new Harmony(PluginGuid);
        
    private void Awake() {
        Logger = base.Logger;
        APClient = new ArchipelagoClient();
        ArchipelagoConsole.Awake();
        ArchipelagoConsole.LogMessage($"{ModDisplayInfo} loaded!");

        SceneManager.sceneLoaded += OnSceneLoaded;
        
        this._harmony.PatchAll();
    }

    private void OnSceneLoaded(Scene scene, LoadSceneMode mode)
    {
        Logger.LogInfo($"Scene loaded: {scene.name}");
    }

    private void OnGUI() {
        // show in the corner that the mod is currently loaded
        GUI.Label(new Rect(16, 16, 300, 20), ModDisplayInfo);
        ArchipelagoConsole.OnGUI();

        // show the Archipelago version and whether we're connected or not
        string statusMessage;
        if (ArchipelagoClient.Authenticated) {
            // if your game doesn't usually show the cursor this line may be necessary
            Cursor.visible = false;

            statusMessage = " Status: Connected";
            GUI.Label(new Rect(16, 40, 300, 20), APDisplayInfo + statusMessage);
        }
        else {
            // if your game doesn't usually show the cursor this line may be necessary
            Cursor.visible = false;
            
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
        while (ArchipelagoClient.TryGetReceivedItem(out string itemName))
            GrantItem(itemName);
    }

    private void GrantItem(string itemName) {
        var languageTypes = new Dictionary<string, LanguageType>() {
            { "Devotee", LanguageType.DEVOTS },
            { "Warrior", LanguageType.GUERRIERS },
            { "Bard", LanguageType.BARDES },
            { "Alchemist", LanguageType.ALCHIMISTES },
            { "Anchorite", LanguageType.RECLUS },
        };

        var itemParts = itemName.Split(' ');

        // Handle runes
        if (itemParts.Length == 3) {
            if (itemParts[1] == "Rune") {
                GameController.GetInstance().GetLanguageController().GetLanguageData(languageTypes[itemParts[0]])
                    .AddRuneIfUnknown(int.Parse(itemParts[2]) - 1);
            }
        }
        
    }
}
