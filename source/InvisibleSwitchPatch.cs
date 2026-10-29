using HarmonyLib;

namespace ChantsOfSennaarAP;

[HarmonyPatch(typeof(InvisibleSwitch))]
static class InvisibleSwitchPatch
{
    [HarmonyPatch(nameof(InvisibleSwitch.Trigger))]
    [HarmonyPrefix]
    static bool SkipTutorialWalkback(InvisibleSwitch __instance) {
        if (__instance.gameObject.scene.name != "A04_Vannes" ||
            __instance.name != "BlocDoorInvisibleSwitch")
            return true;

        return GameController.GetInstance().GetLanguageController()
            .GetLanguageData(LanguageType.DEVOTS).IsValidPage(0);
    }
}