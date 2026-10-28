using HarmonyLib;

namespace ChantsOfSennaarAP;

[HarmonyPatch(typeof(GameController))]
internal class GameControllerPatch {
    [HarmonyPatch(nameof(GameController.Init))]
    [HarmonyPostfix]
    static void ShowClientGUI(GameController __instance) {
        Plugin.SplashFinished = true;
        ArchipelagoConsole.LogMessage($"{Plugin.ModDisplayInfo} loaded!");
    }
}