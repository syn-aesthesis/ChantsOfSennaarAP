using HarmonyLib;

namespace ChantsOfSennaarAP;

[HarmonyPatch(typeof(LanguageController))]
internal class LanguageControllerPatch {
    [HarmonyPatch(nameof(LanguageController.Load))]
    [HarmonyPostfix]
    static void ResetOnLoad(LanguageController __instance) {
        ArchipelagoClient.ResetItemsApplied();
    }
}