from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Item, ItemClassification
if TYPE_CHECKING:
    from .world import ChantsOfSennaarWorld


ITEM_NAME_TO_ID = {
    "Devotee Rune 10": 110,
    "Devotee Rune 11": 111,
    "Devotee Rune 19": 119,
    "[unreadable]": 1001,
    "Bonk": 1002
}


DEFAULT_ITEM_CLASSIFICATIONS = {
    "Devotee Rune 10": ItemClassification.progression,
    "Devotee Rune 11": ItemClassification.progression,
    "Devotee Rune 19": ItemClassification.progression,
    "[unreadable]": ItemClassification.filler,
    "Bonk": ItemClassification.trap
}


class ChantsOfSennaarItem(Item):
    game = "Chants of Sennaar"


def get_random_filler_item_name(world: ChantsOfSennaarWorld) -> str:
    if world.random.randint(0, 99) < world.options.trap_chance:
        return "Bonk"
    return "[unreadable]"


def create_item_with_correct_classification(world: ChantsOfSennaarWorld, name: str) -> ChantsOfSennaarItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return ChantsOfSennaarItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: ChantsOfSennaarWorld) -> None:
    itempool: list[Item] = [
        world.create_item("Devotee Rune 10"),
        world.create_item("Devotee Rune 11"),
        world.create_item("Devotee Rune 19")
    ]

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool