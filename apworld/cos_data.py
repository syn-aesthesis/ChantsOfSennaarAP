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
    "Abbey Great Door 1",
    "Abbey Great Door 2",
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
FORTRESS_SCENES = [
    "Fortress Corridor",
    "Fortress Triage",
    "Fortress Central South",
    "Frontier 1",
    "Frontier 2",
    "Frontier 3",
    "Frontier Precinct",
    "Terminal 3",
    "Frontier Cliff",
    "Fortress Grand Hall",
    "Fortress Grand Hall Stairway",
    "Fortress Garrison",
    "Fortress Warehouse",
    "Fortress Reserve",
    "Fortress Barracks",
    "Fortress Central North",
    "Fortress Armory",
    "Fortress Pit",
    "Fortress Antechamber",
    "Fortress Axle",
    "Fortress Treasury",
    "Terminal 4",
    "Fortress Concourse",
    "Fortress Bridge",
    "Fortress Observatory",
    "Fortress Telescope",
    "Fortress Bells",
    "Fortress Lodging",
    "Fortress Chosen Hall",
    "Fortress Platform",
    "Fortress Barracks West",
    "Fortress Purple Door",
]
GARDENS_SCENES = []
FACTORY_SCENES = []
EXILE_SCENES = []
SCENE_REGIONS = ABBEY_SCENES + FORTRESS_SCENES + GARDENS_SCENES + \
    FACTORY_SCENES + EXILE_SCENES

DEVOTEE_RUNES = [f"Devotee Rune {(r+1):02d}" for r in range(34)]
WARRIOR_RUNES = [f"Warrior Rune {(r+1):02d}" for r in range(36)]
BARD_RUNES = []
ALCHEMIST_RUNES = []
ANCHORITE_RUNES = []
RUNE_REGIONS = DEVOTEE_RUNES + WARRIOR_RUNES + BARD_RUNES + ALCHEMIST_RUNES + \
    ANCHORITE_RUNES

DEVOTEE_PAGES = [
    "Devotee Journal Page: Valves",
    "Devotee Journal Page: Sluices",
    "Devotee Journal Page: Reliefs",
    "Devotee Journal Page: Hide-and-Seek",
    "Devotee Journal Page: Infiltration",
    "Devotee Journal Page: Statues",
    "Devotee Journal Page: Places",
    "Devotee Journal Page: Preacher",
    "Devotee Journal Page: Workshop",
    "Devotee Journal Page: Shops"
]
WARRIOR_PAGES = [
    "Warrior Journal Page: Shield",
    "Warrior Journal Page: Patrol",
    "Warrior Journal Page: Statues",
    "Warrior Journal Page: Cart",
    "Warrior Journal Page: Reserve",
    "Warrior Journal Page: Barracks",
    "Warrior Journal Page: Constellations",
    "Warrior Journal Page: Treasury",
    "Warrior Journal Page: Grimoire",
    "Warrior Journal Page: Music",
    "Warrior Journal Page: Specialist"
]
BARD_PAGES = []
ALCHEMIST_PAGES = []
ANCHORITE_PAGES = []
PAGE_REGIONS = DEVOTEE_PAGES + WARRIOR_PAGES + BARD_PAGES + ALCHEMIST_PAGES + \
    ANCHORITE_PAGES

ALL_REGIONS = SCENE_REGIONS + RUNE_REGIONS + PAGE_REGIONS


ABBEY_SCENE_IDS = [f"A{(i+1):02d}" for i in range(7)] + ["A08a", "A08b"] + \
    [f"A{(i+1):02d}" for i in range(8, len(ABBEY_SCENES))]
FORTRESS_SCENE_IDS = [f"B{(i+1):02d}" for i in range(len(FORTRESS_SCENES))]
GARDENS_SCENE_IDS = [f"C{(i+1):02d}" for i in range(len(GARDENS_SCENES))]
FACTORY_SCENE_IDS = [f"D{(i+1):02d}" for i in range(len(FACTORY_SCENES))]
EXILE_SCENE_IDS = [f"D{(i+1):02d}" for i in range(len(EXILE_SCENES))]

SCENE_IDS = ABBEY_SCENE_IDS + FORTRESS_SCENE_IDS + GARDENS_SCENE_IDS + \
    FACTORY_SCENE_IDS + EXILE_SCENE_IDS


ABBEY_IDS_TO_SCENES = dict(zip(ABBEY_SCENE_IDS, ABBEY_SCENES))
FORTRESS_IDS_TO_SCENES = dict(zip(FORTRESS_SCENE_IDS, FORTRESS_SCENES))
GARDENS_IDS_TO_SCENES = dict(zip(GARDENS_SCENE_IDS, GARDENS_SCENES))
FACTORY_IDS_TO_SCENES = dict(zip(FACTORY_SCENE_IDS, FACTORY_SCENES))
EXILE_IDS_TO_SCENES = dict(zip(EXILE_SCENE_IDS, EXILE_SCENES))

IDS_TO_SCENES = ABBEY_IDS_TO_SCENES | FORTRESS_IDS_TO_SCENES | \
    GARDENS_IDS_TO_SCENES | FACTORY_IDS_TO_SCENES | EXILE_IDS_TO_SCENES


ABBEY_SCENE_ENTRANCES = {
    "A01": ["A02"],
    "A02": ["A01", "A03"],
    "A03": ["A02", "A04"],
    "A04": ["A03", "A05"],
    "A05": ["A04", "A06"],
    "A06": ["A05", "A07"],
    "A07": ["A06", "A08a"],
    "A08a": ["A07", "A08b", "A09", "A10", "A17"],
    "A08b": ["A08a", "A28", "B04"],
    "A09": ["A08a"],
    "A10": ["A08a", "A11", "A12"],
    "A11": ["A10"],
    "A12": ["A10", "A30"],
    "A13": ["A16", "A20", "A22"],
    "A14": ["A13"],
    "A15": ["A18", "A19", "A21", "A23"],
    "A16": ["A13", "A23", "A31"],
    "A17": ["A08a"],
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
    "A28": ["A08b", "A27", "A29"],
    "A29": ["A28"],
    "A30": ["A12", "A19"],
    "A31": ["A16"],  # E21
}
FORTRESS_SCENE_ENTRANCES = {
    "B01": ["B12", "B13"],
    "B02": ["B03", "B18"],
    "B03": ["B02", "B16", "B21", "B25"],
    "B04": ["A08b", "B05"],
    "B05": ["B04", "B06"],
    "B06": ["B05", "B07"],
    "B07": ["B06", "B08"],  # B10, B33?
    "B08": ["B07", "B09"],
    "B09": ["B08", "B10"],
    "B10": ["B09", "B11", "B12", "B32"],  # B07
    "B11": ["B10"],
    "B12": ["B01", "B10", "B17"],
    "B13": ["B01", "B14"],
    "B14": ["B13", "B14", "B15"],
    "B15": ["B14", "B17", "B31"],
    "B16": ["B03", "B14", "B23", "B31"],
    "B17": ["B12", "B15"],
    "B18": ["B02", "B19"],
    "B19": ["B18", "B20", "B21"],
    "B20": ["B19", "B22"],
    "B21": ["B03", "B19"],
    "B22": ["B20"],
    "B23": ["B16", "B24"],
    "B24": ["B23", "B27", "B29"],
    "B25": ["B03", "B26"],
    "B26": ["B25"],
    "B27": ["B24", "B28"],
    "B28": ["B27"],
    "B29": ["B24", "B30"],
    "B30": ["B09"],  # C01
    "B31": ["B15", "B16"],
    "B32": ["B10"],  # E22
}
GARDENS_SCENE_ENTRANCES = {}
FACTORY_SCENE_ENTRANCES = {}
EXILE_SCENE_ENTRANCES = {}

SCENE_ENTRANCES = ABBEY_SCENE_ENTRANCES | FORTRESS_SCENE_ENTRANCES | \
    GARDENS_SCENE_ENTRANCES | FACTORY_SCENE_ENTRANCES | EXILE_SCENE_ENTRANCES


ABBEY_RUNE_ENTRANCES = {
    "A03": [("Devotee", [9, 10, 18])],
    "A04": [("Devotee", [9, 10])],
    "A06": [("Devotee", [3, 4, 9, 10, 12, 16, 18, 22])],
    "A07": [("Devotee", [0, 2, 3, 4, 5, 6, 10, 11, 14, 15, 18, 21, 22, 27, 28])],
    "A08a": [("Devotee", [0, 1, 3, 4, 5, 6, 10, 11, 12, 14, 15, 16, 18, 21]), 
            ("Warrior", [1, 14, 18, 20])],
    "A09": [("Devotee", [0, 5, 6, 27])],
    "A10": [("Devotee", [1, 3, 4, 12, 14, 22, 26, 31])],
    "A11": [("Devotee", [3, 4, 15])],
    "A12": [("Devotee", [1, 3, 4, 5, 12, 13, 21])],
    "A13": [("Devotee", [0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 15, 16, 21, 24, 27])],
    "A14": [("Devotee", [0, 5, 6, 27])],
    "A15": [("Devotee", [0, 3, 4, 11])],
    "A16": [("Devotee", [0, 3, 4, 8, 30])],
    "A19": [("Devotee", [22])],
    "A20": [("Devotee", [23, 24, 25])],
    "A21": [("Devotee", [3, 4, 8, 15, 17, 20, 22, 29, 30, 32, 33])],
    "A22": [("Devotee", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
                         16, 17, 18, 20, 23, 24, 25, 26, 27, 28, 29])],
    "A23": [("Devotee", [1, 2, 3, 7, 8, 14, 24, 28])],
    "A24": [("Devotee", [0, 3, 7, 12, 14, 19, 21, 25, 32])],
    "A27": [("Devotee", [0, 3, 4, 13, 15, 16, 23, 25])],
    "A30": [("Devotee", [1, 3, 4, 5, 10, 12, 14, 15, 17, 18, 21, 31])],
}
FORTRESS_RUNE_ENTRANCES = {
    "B01": [("Warrior", [1, 4, 13, 20])],
    "B02": [("Warrior", [1, 3, 5, 7, 8, 9, 12, 13, 19, 20, 21, 22, 23, 29])],
    "B03": [("Warrior", [2, 4, 5, 10, 13, 14, 17, 20, 28, 29])],
    "B07": [("Warrior", [1, 4, 9, 11, 13, 20])],
    "B08": [("Devotee", [1, 2, 6, 8]),
            ("Warrior", [0, 13, 17, 18, 20])],
    "B10": [("Warrior", [1, 4, 9, 10, 13, 14, 20, 21, 23, 24])],
    "B12": [("Warrior", [3, 20])],
    "B13": [("Warrior", [1, 4, 7, 8, 12, 13, 19, 20, 21, 22, 23])],
    "B14": [("Warrior", [5, 7, 20])],
    "B15": [("Warrior", [3, 9, 20])],
    "B16": [("Warrior", [2, 3, 4, 5, 10, 13, 14, 17, 20, 29])],
    "B18": [("Warrior", [2, 9, 10, 11, 13, 14, 20, 30])],
    "B19": [("Warrior", [29])],
    "B21": [("Devotee", [15, 16]),
            ("Warrior", [33, 34, 35])],
    "B24": [("Warrior", [10, 20])],
    "B26": [("Warrior", [16, 27, 29])],
    "B27": [("Warrior", [0, 5, 28])],
    "B28": [("Warrior", [2, 6, 9, 10, 15, 16, 20, 25, 26, 27])],
    "B29": [("Warrior", [2, 3, 4, 10, 13, 15, 17, 18, 20, 21, 32])],
    "B30": [("Warrior", [15, 30, 31])],
    "B31": [("Warrior", [3, 9, 10, 13, 14, 20, 21, 23, 24])],
}
GARDENS_RUNE_ENTRANCES = {}
FACTORY_RUNE_ENTRANCES = {}
EXILE_RUNE_ENTRANCES = {}

RUNE_ENTRANCES = ABBEY_RUNE_ENTRANCES | FORTRESS_RUNE_ENTRANCES | \
    GARDENS_RUNE_ENTRANCES | FACTORY_RUNE_ENTRANCES | EXILE_RUNE_ENTRANCES


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

PROG_KEY_ITEMS = ["Cellar Key", "Lens", "Workshop Key", "Coin", "Filter", "Bottle"]
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
    match page_lang:
        case "Devotee":
            page_num = DEVOTEE_PAGES.index(page)
        case "Warrior":
            page_num = WARRIOR_PAGES.index(page)
        case "Bard":
            page_num = BARD_PAGES.index(page)
        case "Alchemist":
            page_num = ALCHEMIST_PAGES.index(page)
        case "Anchorite":
            page_num = ANCHORITE_PAGES.index(page)
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
    filler = FILLER_KEY_ITEMS[f]
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
]
DEVOTEE_PAGE_SCENES = [
    ["A04"],
    ["A06"],
    ["A07", "A08a"],  # OR, not AND
    ["A07", "A08a", "A10", "A11"],
    ["A19"],
    ["A15", "A16", "A27"],
    ["A10", "A22", "A23", "A27"],
    ["A22"],
    ["A21", "A23", "A24", "A30"],
    ["A16", "A21"],
]

WARRIOR_PAGE_RUNES = [
    [0, 13, 17, 18],
    [1, 4, 20],
    [10, 14, 24],
    [21, 22, 23],
    [5, 7, 12, 19],
    [3, 8, 9],
    [6, 15, 25, 26],
    [2, 11, 29],
    [16, 27, 28],
    [30, 31, 32],
    [33, 34, 35]
]
WARRIOR_PAGE_SCENES = [
    ["B08"],
    ["B10"],
    ["B10"],  # check conditions for operating statue
    ["B13"],
    ["B14"],
    ["B31"],
    ["B19"],
    ["B21"],
    ["B26", "B28"],
    ["B30"],
    ["B21"]
]
