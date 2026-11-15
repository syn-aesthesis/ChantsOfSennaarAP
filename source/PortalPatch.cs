using HarmonyLib;
using System.Linq;
using UnityEngine;

namespace ChantsOfSennaarAP;

[HarmonyPatch(typeof(Portal))]
internal class PortalPatch {
    [HarmonyPatch(nameof(Portal.IsOpen))]
    [HarmonyPostfix]
    static void RequirePortalKeys(Portal __instance, ref bool __result) {
        if (__result && IsBlocked(__instance))
            __result = false;
    }
    
    [HarmonyPatch(nameof(Portal.Launch))]
    [HarmonyPrefix]
    static bool BlockLaunch(Portal __instance) => !IsBlocked(__instance);

    private static bool IsBlocked(Portal p) {
        if (Plugin.PortalGates.Count == 0 || p.respanwPortal)
            return false;

        var gc = GameController.GetInstance();
        var link = p.GetLinkedPortalLoader();
        if (gc == null || link == null)
            return false;

        var srcId = gc.GetPlaceController().GetPlaceId(p.GetPlace());
        var src = (srcId.level, srcId.id);
        var dst = (link.level, link.placeId);

        if (!Plugin.PortalGates.TryGetValue((src, dst), out var keyGroups))
            return false;

        if (keyGroups.Any(g => g.All(Plugin.ReceivedPortalKeys.Contains)))
            return false;

        return true;
    }
}