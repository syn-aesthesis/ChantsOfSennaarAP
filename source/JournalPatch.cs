using HarmonyLib;
using System.Collections.Generic;
using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.Packets;

namespace ChantsOfSennaarAP;

[HarmonyPatch(typeof(Journal))]
internal class JournalPatch
{
    private static readonly Dictionary<string, string> Languages = new Dictionary<string, string>() {
        { "DEVOTS", "Devotee" },
        { "GUERRIERS", "Warrior" },
        { "BARDES", "Bard"},
        { "ALCHIMISTES", "Alchemist"},
        { "RECLUS", "Anchorite"},
    };
    
    [HarmonyPatch(nameof(Journal.ValidPage), new[] { typeof(JournalSlotUI[]) })]
    [HarmonyPostfix]
    static void CompletePage(Journal __instance, ref JournalSlotUI[] slots) {
        LanguageType lang = default;
        int pageId = -1;
        
        for (int l = 0; l < 5; l++) {
            var langUI = __instance.GetJournalLanguageUI((LanguageType)l);
            for (int p = 0; p < langUI.pages.Length; p++) {
                if (ReferenceEquals(langUI.pages[p].GetPageSlots(), slots)) {
                    lang = (LanguageType)l;
                    pageId = p;
                }
            }
        }

        if (pageId == -1)
            return;
        
        Plugin.Logger.LogInfo($"Completed page: " +
                              $"{lang} {pageId}");
        
        ArchipelagoClient.SendCheck($"Complete {Languages[lang.ToString()]} Journal Page {(pageId+1):00}");
        
        // TODO: Revise to check goal_type and journal_hunt_page_count settings before goaling
        ArchipelagoClient.SendGoalPacket();
    }
}