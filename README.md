# Chants of Sennaar AP

An [Archipelago Multiworld](https://github.com/ArchipelagoMW/Archipelago) implementation for Chants of Sennaar

- **Status:** Playable alpha, unstable
- **Latest release:** 0.2.1 (improved Floor 1 implementation)


## Mod installation guide (Windows)

1. Download the ZIP for [BepInEx 5.4 (win-x64)](https://github.com/BepInEx/BepInEx/releases).
2. Extract the contents of this ZIP into your Chants of Sennaar game directory.
3. Launch and then close the game. This should initialise BepInEx and create a `BepInEx/plugins` folder in your game directory.
4. Download the ZIP containing the latest release of this mod.
5. Extract the ChantsOfSennaarAP folder into the `BepInEx/plugins` folder inside your game directory.
6. Launch the game. The AP mod menu should now appear on start-up.


## About this AP implementation

What is currently implemented?
- Versions 0.2.x contain the initial implementation of Floor 1.

What do the yaml options do?
- In Versions 0.2.x, the `goal_type` is fixed to `journal_hunt` with a `journal_hunt_page_count` ranging from 1 to 10. Any other options selected do not currently affect the behavior of the mod.

What count as "checks" in this game?
- Each new rune observed is one check.
- Each journal page completed is one check.
- Terminal puzzles are planned as optional checks in a future update.

What "items" can you receive?
- Runes and key items are implemented as AP items that can be received from the multiworld.
- Terminal "keys" are planned as optional items in a future update.

What else is randomized in this game?
- Randomized start locations are planned in a future update.
- A language randomization system has been proposed, and may be implemented at a much later stage.


## AI usage disclosure

- This implementation is not vibe-coded.
- This implementation does not contain any AI-generated media assets.
- I have used AI capabilities common to IDEs including inline code completion, proactive error detection, and semantic refactoring. I review all such modifications for intended functionality and syntax before committing any code.
- I have used an AI platform as a tool for reviewing my first-draft code to flag security or style issues and suggest revisions. I review the line-by-line behavior of any such code suggestions, consult primary documentation for all unfamiliar syntax and components, and run independent tests before committing any revisions to source.
- This mod depends on files and templates from the [BepInEx modding framework](https://github.com/BepInEx/BepInEx) and [Archipelago.MultiClient.Net library](https://github.com/ArchipelagoMW/Archipelago.MultiClient.Net). I cannot personally verify the extent to which these external projects may or may not have used AI in their development.



## Contributing

Bug reports, design suggestions, and other inputs related to this AP implementation are welcome in the Chants of Sennaar thread on the Archipelago Discord server.
