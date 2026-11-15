using HarmonyLib;

namespace ChantsOfSennaarAP;

[HarmonyPatch(typeof(TutorialUI))]
internal static class TutorialUIPatch {
    private static bool seen;

    [HarmonyPatch("HasOpen")]
    [HarmonyPrefix]
    private static bool SkipOnSeen(TutorialUI.TutorialState ___state, ref bool __result) {
        if (seen && ___state == TutorialUI.TutorialState.WAIT_FIRST_VALID) {
            __result = true;
            return false;
        }

        return true;
    }

    [HarmonyPatch(nameof(TutorialUI.Loop))]
    [HarmonyPostfix]
    private static void RecordSeen(TutorialUI __instance, TutorialUI.TutorialState ___state) {
        if (___state == TutorialUI.TutorialState.WAIT_FIRST_VALID &&
            __instance.waitFirstValidTuto.gameObject.activeSelf)
            seen = true;
    }
}