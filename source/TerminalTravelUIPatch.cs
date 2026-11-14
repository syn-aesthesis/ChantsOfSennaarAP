using HarmonyLib;

namespace ChantsOfSennaarAP;

[HarmonyPatch(typeof(TerminalTravelUI))]
internal class TerminalTravelUIPatch {
    private static readonly AccessTools.FieldRef<TerminalTravelUI, int> TerminalNumero =
        AccessTools.FieldRefAccess<TerminalTravelUI, int>("terminalNumero");
    private static readonly AccessTools.FieldRef<TerminalTravelUI, bool> Selected = 
        AccessTools.FieldRefAccess<TerminalTravelUI, bool>("selected");

    [HarmonyPatch(nameof(TerminalTravelUI.Display))]
    [HarmonyPrefix]
    static bool SuppressDisplay(TerminalTravelUI __instance, bool newSelected) {
        if (!newSelected)
            return true;

        var loader = __instance.travelButtons[TerminalNumero(__instance)].terminalTarget.terminalLoader;
        var key = (loader.level, loader.placeId);
        if (!Plugin.TerminalItems.ContainsValue(key) || Plugin.ReceivedTerminals.Contains(key))
            return true;

        Selected(__instance) = true;  // keep terminal on TRAVEL tab but suppress display
        return false;
    }
}
