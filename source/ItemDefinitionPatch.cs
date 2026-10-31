using HarmonyLib;

namespace ChantsOfSennaarAP; 

[HarmonyPatch(typeof(ItemDefinition))]
internal class ItemDefinitionPatch {
    [HarmonyPatch(nameof(ItemDefinition.IsOwned), new[] { typeof(bool) })]
    [HarmonyPostfix]
    static void RequireReceived(ItemDefinition __instance, ref bool __result) {
        if (__result && Plugin.ItemTypes.ContainsValue(__instance.itemType)
            && !Plugin.ReceivedItems.Contains(__instance.itemType))
            __result = false;
    }
}