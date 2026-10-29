using System.Diagnostics;
using HarmonyLib;

namespace ChantsOfSennaarAP;

[HarmonyPatch(typeof(PlayerController))]
internal class PlayerControllerPatch 
{
    [HarmonyPatch(nameof(PlayerController.AddPageToRevele), new[] { typeof(PageRevelator) })]
    [HarmonyPrefix]
    static bool SkipTutorialJournalReopen(PlayerController __instance, ref PageRevelator pageRevelator) {
        if (pageRevelator.language != LanguageType.DEVOTS || pageRevelator.pageId != 0)
            return true;

        var data = GameController.GetInstance().GetLanguageController()
            .GetLanguageData(LanguageType.DEVOTS);

        bool complete = data.IsValidPage(0);
        bool neverShown = data.CanRevelePage(0);
        Plugin.Logger.LogDebug($"DEVOT page 0 complete={complete}, neverShown={neverShown}" +
                               $"autoValidate={pageRevelator.autoValidate}");

        if (complete)  // vanilla
            return true;
        if (neverShown) // give page without opening journal 
            data.RevelePage(0, allowSeveralWrite: false, autoValidate: false, forceOpen: false);

        return false;
    }
}