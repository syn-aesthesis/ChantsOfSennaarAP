# Chants of Sennaar AP

An [Archipelago Multiworld](https://github.com/ArchipelagoMW/Archipelago) implementation for Chants of Sennaar

- **Status:** Playable alpha, unstable
- **Latest release:** 0.2.0 (Floor 1 implementation)


## Mod installation guide (Windows)

1. Download the ZIP for [BepInEx 5.4 (win-x64)](https://github.com/BepInEx/BepInEx/releases)
2. Extract the contents of this ZIP into your Chants of Sennaar directory
3. Download the ZIP containing the latest release of this mod
4. Extract the ChantsOfSennaarAP folder into the `bepinex/plugins` folder inside your Chants of Sennaar directory
5. Launch Chants of Sennaar


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
- Floor access "keys" are planned as optional items in a future update.

What else is randomized in this game?
- Randomized start locations are planned in a future update.
- A language randomization system has been proposed, and may be implemented at a much later stage.


## AI usage disclosure

- This implementation is not vibe-coded.
- This implementation does not contain any AI-generated images, 3D models, or music.
- I write source code in an IDE with light AI functionalities, which I use to complete lines, correct typos, and refactor variable names. I review any such modifications for correct syntax and functionality prior to committing any code.
- I use LLM tools to better understand software engineering practices and specific functionalities of common frameworks and libraries that are unfamiliar to me. I cross-check this information against published documentation and credible source materials.
- This mod depends on files and templates from the [BepInEx modding framework](https://github.com/BepInEx/BepInEx) and [Archipelago.MultiClient.Net library](https://github.com/ArchipelagoMW/Archipelago.MultiClient.Net). I cannot personally verify the extent to which these external projects may or may not have used AI in their development.



## Contributing

Bug reports, design suggestions, and other inputs related to this AP implementation are welcome in the Chants of Sennaar thread on the Archipelago Discord server.
