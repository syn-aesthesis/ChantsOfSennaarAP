from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld
# from .options import option_groups, option_presets


class ChantsOfSennaarWebWorld(WebWorld):
    game = "Chants of Sennaar"

    theme = "ocean"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Chants of Sennaar for Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["synaesthesis"],
    )

    tutorials = [setup_en]

    # option_groups = option_groups
    # options_presets = option_presets