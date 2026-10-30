from __future__ import annotations
from typing import TYPE_CHECKING
from rule_builder.rules import (
    Has, HasAll, CanReachLocation, CanReachRegion, AtLeast, And
)
if TYPE_CHECKING:
    from .world import ChantsOfSennaarWorld

from .cos_data import *


def set_all_rules(world: ChantsOfSennaarWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: ChantsOfSennaarWorld) -> None:
    # set scene access conditions

    world.set_rule(  # A13 -> A22
        world.get_entrance("Abbey Forecourt to Abbey Church"),
        Has("Lens")  # TODO: separate church runes into two regions
    )
    world.set_rule(  # A23 -> A24
        world.get_entrance("Abbey Garden to Abbey Workshop"),
        Has("Workshop Key")
    )
    world.set_rule(  # A28 -> A29
        world.get_entrance("Abbey Underground 1 to Abbey Underground 2"),
        Has("Lens")
    )
    world.set_rule(  # A30 -> A19
        world.get_entrance("Abbey Cellar to Abbey Cloister"),
        Has("Cellar Key")
    )

    # set journal page conditions
    origin = world.origin_region_name
    for p in range(len(DEVOTEE_PAGES)):
        page_name = DEVOTEE_PAGES[p]
        page_runes = [f"Devotee Rune {r+1:02d}" for r in DEVOTEE_PAGE_RUNES[p]]
        page_scenes = [
            f"{ABBEY_IDS_TO_SCENES[s]}" for s in DEVOTEE_PAGE_SCENES[p]
        ]
        world.set_rule(
            world.get_entrance(f"{origin} to {page_name}"), 
            And(
                HasAll(*page_runes),
                *[CanReachRegion(scene) for scene in page_scenes],
            )
        )


def set_all_location_rules(world: ChantsOfSennaarWorld) -> None:
    goal_location = world.get_location("Goal Condition")

    page_count = world.options.journal_hunt_page_count.value
    can_reach_goal = AtLeast(
        page_count, 
        *[CanReachLocation(f"Complete {page}") for page in PAGE_REGIONS]
    )
    world.set_rule(goal_location, can_reach_goal)


def set_completion_condition(world: ChantsOfSennaarWorld) -> None:
    world.set_completion_rule(Has("Goal"))
