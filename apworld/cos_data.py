from BaseClasses import ItemClassification


# ----- regions.py -----

ABBEY_SCENES = [
    "Crypt Spawn",
    "Crypt Stairway",
    "Crypt Sewer Gate",
    "Crypt Valves",
    "Crypt Sewer Viaduct",
    "Crypt Sluices",
    "Abbey Gallery",
    "Abbey Great Door",
    "Abbey Card Game",
    "Abbey Esplanade",
    "Abbey Terrace",
    "Abbey Courtyard",
    "Abbey Forecourt",
    "Abbey Forecourt Puzzle",
    "Abbey East",
    "Abbey North",
    "Terminal 1",
    "Abbey Warehouse",
    "Abbey Cloister",
    "Abbey Crossroads",
    "Abbey Shops",
    "Abbey Church",
    "Abbey Garden",
    "Abbey Workshop",
    "Abbey Alley",
    "Terminal 2",
    "Abbey Cemetery",
    "Abbey Underground 1",
    "Abbey Underground 2",
    "Abbey Cellar",
    "Abbey Purple Door",
]
FORTRESS_SCENES = []
GARDENS_SCENES = []
FACTORY_SCENES = []
EXILE_SCENES = []
SCENE_REGIONS = ABBEY_SCENES + FORTRESS_SCENES + GARDENS_SCENES + \
    FACTORY_SCENES + EXILE_SCENES

DEVOTEE_RUNES = [f"Devotee Rune {(r+1):02d}" for r in range(34)]
WARRIOR_RUNES = [f"Warrior Rune {(r+1):02d}" for r in [1, 14, 18, 20]]
BARD_RUNES = []
ALCHEMIST_RUNES = []
ANCHORITE_RUNES = []
RUNE_REGIONS = DEVOTEE_RUNES + WARRIOR_RUNES + BARD_RUNES + ALCHEMIST_RUNES + \
    ANCHORITE_RUNES

DEVOTEE_PAGES = [f"Devotee Journal Page {(p+1):02d}" for p in range(11)]
WARRIOR_PAGES = []
BARD_PAGES = []
ALCHEMIST_PAGES = []
ANCHORITE_PAGES = []
PAGE_REGIONS = DEVOTEE_PAGES + WARRIOR_PAGES + BARD_PAGES + ALCHEMIST_PAGES + \
    ANCHORITE_PAGES

ALL_REGIONS = SCENE_REGIONS + RUNE_REGIONS + PAGE_REGIONS


ABBEY_SCENE_IDS = [f"A{(i+1):02d}" for i in range(31)]
ABBEY_IDS_TO_SCENES = dict(zip(ABBEY_SCENE_IDS, ABBEY_SCENES))
ABBEY_SCENE_ENTRANCES = {
    "A01": ["A02"],
    "A02": ["A01", "A03"],
    "A03": ["A02", "A04"],
    "A04": ["A03", "A05"],
    "A05": ["A04", "A06"],
    "A06": ["A05", "A07"],
    "A07": ["A06", "A08"],
    "A08": ["A07", "A09", "A10", "A17"],
    "A09": ["A08"],
    "A10": ["A08", "A11", "A12"],
    "A11": ["A10"],
    "A12": ["A10", "A30"],
    "A13": ["A16", "A20", "A22"],
    "A14": ["A13"],
    "A15": ["A18", "A21", "A23"],
    "A16": ["A13", "A23", "A31"],
    "A17": ["A08"],
    "A18": ["A15", "A21"],
    "A19": ["A15", "A20", "A30"],
    "A20": ["A13", "A19", "A23", "A25"],
    "A21": ["A15", "A18"],
    "A22": ["A13"],
    "A23": ["A15", "A16", "A20", "A24"],
    "A24": ["A23"],
    "A25": ["A20", "A26", "A27"],
    "A26": ["A25"],
    "A27": ["A25", "A28"],
    "A28": ["A27", "A29"],  # B04
    "A29": ["A28"],
    "A30": ["A12", "A19"],
    "A31": ["A16"],  # E21
}
ABBEY_RUNE_ENTRANCES = {
    "A03": [("Devotee", [9, 10, 18])],
    "A04": [("Devotee", [9, 10])],
    "A06": [("Devotee", [3, 4, 9, 10, 12, 16, 18, 22])],
    "A07": [("Devotee", [0, 2, 4, 5, 6, 10, 11, 14, 15, 18, 21, 22, 27, 28])],
    "A08": [("Devotee", [0, 1, 3, 4, 5, 12, 14, 15, 18, 21]), 
            ("Warrior", [1, 14, 18, 20])],
    "A09": [("Devotee", [0, 5, 6, 27])],
    "A10": [("Devotee", [1, 3, 4, 14, 26, 31])],
    "A11": [("Devotee", [3, 4, 15])],
    "A12": [("Devotee", [1, 3, 4, 5, 13])],
    "A13": [("Devotee", [0, 1, 2, 3, 4, 5, 6, 15, 16, 21, 27])],
    "A14": [("Devotee", [0, 5, 6, 27])],
    "A15": [("Devotee", [0, 3, 4, 11])],
    "A16": [("Devotee", [0, 3, 4, 8, 30])],
    "A19": [("Devotee", [22])],
    "A20": [("Devotee", [23, 24, 25])],
    "A21": [("Devotee", [3, 17, 20, 22, 29, 32, 33])],
    "A22": [("Devotee", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
                         16, 17, 18, 20, 23, 24, 25, 26, 27, 28, 29])],
    "A23": [("Devotee", [1, 7, 24])],
    "A24": [("Devotee", [0, 3, 7, 12, 14, 19, 21, 25, 32])],
    "A25": [("Devotee", [0, 4, 15])],
    "A27": [("Devotee", [0, 3, 4, 13, 15, 16, 23, 25])],
    "A30": [("Devotee", [1, 3, 4, 12, 14, 17, 21])],
}


# ----- locations.py, items.py -----

LOCATION_NAME_TO_ID = {}
ITEM_NAME_TO_ID = {}
DEFAULT_ITEM_CLASSIFICATIONS = {}

LANG_ID_VAL = {
    "Devotee": 100,
    "Warrior": 200,
    "Bard": 300,
    "Alchemist": 400,
    "Anchorite": 500,
}

PROG_KEY_ITEMS = ["Cellar Key", "Lens", "Workshop Key"]
USEFUL_KEY_ITEMS = []
FILLER_KEY_ITEMS = ["Vase Plan"]

PROG_ITEMS = RUNE_REGIONS + PROG_KEY_ITEMS

TRAP_ITEMS = ["Bonk"]
FILLER_ITEMS = ["Gibberish"]

for rune in RUNE_REGIONS:
    rune_lang = rune.split(' ')[0]
    rune_num = int(rune.split(' ')[-1])
    LOCATION_NAME_TO_ID[f"Observe {rune}"] = LANG_ID_VAL[rune_lang] + rune_num
    ITEM_NAME_TO_ID[rune] = LANG_ID_VAL[rune_lang] + rune_num
    DEFAULT_ITEM_CLASSIFICATIONS[rune] = ItemClassification.progression

for page in PAGE_REGIONS:
    page_lang = page.split(' ')[0]
    page_num = int(page.split(' ')[-1])
    LOCATION_NAME_TO_ID[f"Complete {page}"] = (
        500 + LANG_ID_VAL[page_lang] + page_num
    )

for p in range(len(PROG_KEY_ITEMS)):
    prog = PROG_KEY_ITEMS[p]
    ITEM_NAME_TO_ID[prog] = 2100 + p
    DEFAULT_ITEM_CLASSIFICATIONS[prog] = ItemClassification.progression

for u in range(len(USEFUL_KEY_ITEMS)):
    useful = USEFUL_KEY_ITEMS[u]
    ITEM_NAME_TO_ID[useful] = 2200 + u
    DEFAULT_ITEM_CLASSIFICATIONS[useful] = ItemClassification.useful

for f in range(len(FILLER_KEY_ITEMS)):
    filler = FILLER_ITEMS[f]
    ITEM_NAME_TO_ID[filler] = 2300 + f
    DEFAULT_ITEM_CLASSIFICATIONS[filler] = ItemClassification.filler

for t in range(len(TRAP_ITEMS)):
    trap = TRAP_ITEMS[t]
    ITEM_NAME_TO_ID[trap] = 2400 + t
    DEFAULT_ITEM_CLASSIFICATIONS[trap] = ItemClassification.trap

for f in range(len(FILLER_ITEMS)):
    filler = FILLER_ITEMS[f]
    ITEM_NAME_TO_ID[filler] = 2500 + f
    DEFAULT_ITEM_CLASSIFICATIONS[filler] = ItemClassification.filler


# ----- rules.py -----

DEVOTEE_PAGE_RUNES = [
    [9, 10, 18],
    [3, 4, 22],
    [0, 5, 6, 27],
    [12, 14, 15],
    [1, 21, 31],
    [8, 11, 13, 16],
    [23, 24, 25, 26],
    [2, 7, 28],
    [17, 19, 20, 32],
    [29, 30, 33],
    []
]
