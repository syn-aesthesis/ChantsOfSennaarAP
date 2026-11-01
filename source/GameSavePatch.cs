using System;
using HarmonyLib;

namespace ChantsOfSennaarAP;

[HarmonyPatch(typeof(GameSave))]
internal class GameSavePatch {
    [HarmonyPatch(nameof(GameSave.SavePlaces))]
    [HarmonyPostfix]
    static void SaveItems() {
        try {
            ArchipelagoClient.SaveItemsApplied();
        }
        catch (Exception e) {
            Plugin.Logger.LogError(e);
        }
    }

    [HarmonyPatch(nameof(GameSave.ClearAllData))]
    [HarmonyPostfix]
    static void ResetItemsOnNewGame() {
        try {
            if (ArchipelagoClient.SaveData != null) {
                ArchipelagoClient.SaveData.ItemsApplied = 0;
                ArchipelagoClient.SaveData.Save();
            }

            ArchipelagoClient.ResetItemsApplied();
        }
        catch (Exception e) {
            Plugin.Logger.LogError(e);
        }
    }
}