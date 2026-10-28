using HarmonyLib;

namespace ChantsOfSennaarAP;

[HarmonyPatch(typeof(GameController))]
internal class GameControllerPatch {
    [HarmonyPatch(nameof(GameController.Init))]
    [HarmonyPostfix]
    static void FlagSplashFinished(GameController __instance) {
        Plugin.SplashFinished = true;
    }
}