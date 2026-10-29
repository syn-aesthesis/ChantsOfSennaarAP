from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Item
if TYPE_CHECKING:
    from .world import ChantsOfSennaarWorld

from .cos_data import *


class ChantsOfSennaarItem(Item):
    game = "Chants of Sennaar"


def get_random_filler_item_name(world: ChantsOfSennaarWorld) -> str:
    if world.random.randint(0, 99) < world.options.trap_chance:
        return world.random.choice(TRAP_ITEM_NAMES)
    return world.random.choice(FILLER_ITEM_NAMES)


def create_item_with_correct_classification(world: ChantsOfSennaarWorld, 
                                            name: str) -> ChantsOfSennaarItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return ChantsOfSennaarItem(name, classification, ITEM_NAME_TO_ID[name], 
                               world.player)


def create_all_items(world: ChantsOfSennaarWorld) -> None:
    itempool: list[Item] = [
        world.create_item("Devotee Rune 10"),
        world.create_item("Devotee Rune 11"),
        world.create_item("Devotee Rune 19")
    ]

    num_items = len(itempool)
    num_unfilled = len(world.multiworld.get_unfilled_locations(world.player))
    num_filler_items = num_unfilled - num_items

    itempool += [world.create_filler() for _ in range(num_filler_items)]

    world.multiworld.itempool += itempool
