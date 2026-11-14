using HarmonyLib;
using System.Collections.Generic;

namespace ChantsOfSennaarAP;

[HarmonyPatch(typeof(Journal))]
internal class JournalPatch
{
    private static readonly Dictionary<string, Dictionary<int, string>> Languages = new() {
        { "DEVOTS", new Dictionary<int, string>()
            {
                {0, "Devotee Journal Page: Valves"},
                {1, "Devotee Journal Page: Sluices"},
                {2, "Devotee Journal Page: Reliefs"},
                {3, "Devotee Journal Page: Hide-and-Seek"},
                {4, "Devotee Journal Page: Infiltration"},
                {5, "Devotee Journal Page: Statues"},
                {6, "Devotee Journal Page: Places"},
                {7, "Devotee Journal Page: Preacher"},
                {8, "Devotee Journal Page: Workshop"},
                {9, "Devotee Journal Page: Shops"},
            } 
        },
        { "GUERRIERS", new Dictionary<int, string>()
            {
                {0, "Warrior Journal Page: Shield"},
                {1, "Warrior Journal Page: Patrol"},
                {2, "Warrior Journal Page: Statues"},
                {3, "Warrior Journal Page: Cart"},
                {4, "Warrior Journal Page: Reserve"},
                {5, "Warrior Journal Page: Barracks"},
                {6, "Warrior Journal Page: Constellations"},
                {7, "Warrior Journal Page: Treasury"},
                {8, "Warrior Journal Page: Grimoire"},
                {9, "Warrior Journal Page: Music"},
                {12, "Warrior Journal Page: Specialist"},
            } 
        },
        { "BARDES", new Dictionary<int, string>()
            {
                
            }  
        },
        { "ALCHIMISTES", new Dictionary<int, string>()
            {
                
            }
        },
        { "RECLUS", new Dictionary<int, string>()
            {
                
            }
        },
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
        
        Plugin.Logger.LogInfo($"Completed page: {lang} {pageId}");
        
        ArchipelagoClient.SendCheck($"Complete {Languages[lang.ToString()][pageId]}");
    }
}