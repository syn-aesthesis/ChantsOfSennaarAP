from __future__ import annotations
from typing import TYPE_CHECKING
from rule_builder.rules import Has, HasAll, CanReachLocation, Rule
if TYPE_CHECKING:
    from .world import ChantsOfSennaarWorld

from .cos_data import *


def set_all_rules(world: ChantsOfSennaarWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: ChantsOfSennaarWorld) -> None:
    # set scene exit conditions
    world.set_rule(
        world.get_entrance("Crypt Valves to Crypt Sewer Viaduct"), 
        HasAll("Devotee Rune 10", "Devotee Rune 11", "Devotee Rune 19")
    )

    # set journal page conditions
    for p in len(DEVOTEE_PAGES):
        page_name = DEVOTEE_PAGES[p]
        page_runes = [f"Devotee Rune {r+1}:02d" for r in DEVOTEE_PAGE_RUNES[p]]
        origin = world.origin_region_name
        world.set_rule(
            world.get_entrance(f"{origin} to {page_name}"), 
            HasAll(page_runes)
        )


def set_all_location_rules(world: ChantsOfSennaarWorld) -> None:
    goal_location = world.get_location("Goal Condition")
    can_reach_goal = CanReachLocation("Complete Devotee Journal Page 01")
    world.set_rule(goal_location, can_reach_goal)


def set_completion_condition(world: ChantsOfSennaarWorld) -> None:
    world.set_completion_rule(Has("Goal"))
