using HarmonyLib;
using System.Collections.Generic;

namespace ChantsOfSennaarAP;

[HarmonyPatch(typeof(LanguageData))]
internal class LanguageDataPatch
{
    private static readonly Dictionary<string, string> Languages = new Dictionary<string, string>() {
        { "DEVOTS", "Devotee" },
        { "GUERRIERS", "Warrior" },
        { "BARDES", "Bard"},
        { "ALCHIMISTES", "Alchemist"},
        { "RECLUS", "Anchorite"},
    };
    
    [HarmonyPatch(nameof(LanguageData.AddRuneIfUnknown))]
    [HarmonyPrefix]
    static void ReceiveRune(LanguageData __instance, ref int runeId)
    {
        Plugin.Logger.LogInfo($"Receiving rune: {__instance.GetLanguageType()} {runeId}");
    }

    [HarmonyPatch(nameof(LanguageData.AddRunes), new[] { typeof(int[]) })]
    [HarmonyPrefix]
    static bool ObserveRunes(LanguageData __instance, ref int[] runes)
    {
        // Plugin.Logger.LogInfo($"Observing runes: {__instance.GetLanguageType()} {string.Join(",", runes)}");
        foreach (var rune in runes) {
            ArchipelagoClient.SendCheck($"Observe {Languages[__instance.GetLanguageType().ToString()]} " + 
                                        $"Rune {(rune+1):00}");
        }
        return false;
    }
    
    [HarmonyPatch(nameof(LanguageData.AddRunes), new[] { typeof(SpeechLine) })]
    [HarmonyPrefix]
    static bool ObserveRunes(LanguageData __instance, ref SpeechLine line)
    {
        // Plugin.Logger.LogInfo($"Observing runes: {__instance.GetLanguageType()} {string.Join(",",line.runes)}");
        foreach (var rune in line.runes) {
            ArchipelagoClient.SendCheck($"Observe {Languages[__instance.GetLanguageType().ToString()]} " + 
                                        $"Rune {(rune+1):00}");
        }
        return false;
    }
}
