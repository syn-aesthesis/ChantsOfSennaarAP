using HarmonyLib;

namespace ChantsOfSennaarAP;

[HarmonyPatch(typeof(TerminalDefinition))]
internal class TerminalDefinitionPatch {
    [HarmonyPatch(nameof(TerminalDefinition.IsFound))]
    [HarmonyPostfix]
    static void RequireReceived(TerminalDefinition __instance, ref bool __result) {
        if (!__result)
            return;

        var key = (__instance.terminalLoader.level, __instance.terminalLoader.placeId);
        if (Plugin.TerminalItems.ContainsValue(key) && !Plugin.ReceivedTerminals.Contains(key))
            __result = false;
    }
}
