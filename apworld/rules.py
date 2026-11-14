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
    world.set_rule(  # A08b -> A28
        world.get_entrance("Abbey Great Door 2 to Abbey Underground 1"),
            Has("Lens"),
    )
    world.set_rule(  # A08b -> B04
        world.get_entrance("Abbey Great Door 2 to Frontier 1"),
        Has("Lens")
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
    world.set_rule(  # A28 -> A08b
        world.get_entrance("Abbey Underground 1 to Abbey Great Door 2"),
        Has("Lens")
    )
    world.set_rule(  # B04 -> A08b
        world.get_entrance("Frontier 1 to Abbey Great Door 2"),
        Has("Lens")
    )
    world.set_rule(  # B24 -> B29
        world.get_entrance("Fortress Bridge to Fortress Chosen Hall"),
        Has("Bottle")
    )
    world.set_rule(  # B27 -> B28
        world.get_entrance("Fortress Bells to Fortress Lodging"),
        Has("Bottle")
    )
    # B09 Cliff -> B10 Grand Hall: requires B08 Terminal 3

    # set journal page conditions
    origin = world.origin_region_name
    for p in range(len(DEVOTEE_PAGES)):
        page_name = DEVOTEE_PAGES[p]
        page_runes = [DEVOTEE_RUNES[r] for r in DEVOTEE_PAGE_RUNES[p]]
        page_scenes = [
            f"{IDS_TO_SCENES[s]}" for s in DEVOTEE_PAGE_SCENES[p]
        ]
        world.set_rule(
            world.get_entrance(f"{origin} to {page_name}"), 
            And(
                HasAll(*page_runes),
                *[CanReachRegion(scene) for scene in page_scenes],
            )
        )
    for p in range(len(WARRIOR_PAGES)):
        page_name = WARRIOR_PAGES[p]
        page_runes = [WARRIOR_RUNES[r] for r in WARRIOR_PAGE_RUNES[p]]
        page_scenes = [
            f"{IDS_TO_SCENES[s]}" for s in WARRIOR_PAGE_SCENES[p]
        ]
        world.set_rule(
            world.get_entrance(f"{origin} to {page_name}"), 
            And(
                HasAll(*page_runes),
                *[CanReachRegion(scene) for scene in page_scenes],
            )
        )

    # set rune conditions
    # A07 DEVOTS 3, 4, 14 -- need access to A08a, A11 (child)
    for r in [3, 4, 14]:    
        world.set_rule(
            world.get_entrance(f"{IDS_TO_SCENES["A07"]} to {DEVOTEE_RUNES[r]}"),
            And(
                CanReachRegion(f"{IDS_TO_SCENES["A08a"]}"),
                CanReachRegion(f"{IDS_TO_SCENES["A11"]}")
            )
        )
    # A08a DEVOTS 14 -- need access to A11 (child)
    world.set_rule(
        world.get_entrance(f"{IDS_TO_SCENES["A08a"]} to {DEVOTEE_RUNES[14]}"),
        CanReachRegion(f"{IDS_TO_SCENES["A11"]}")
    )
    # A10 DEVOTS 1, 3, 4, 12, 14, 22, 31 -- need access to A07, A08a, A11 (child)
    for r in [1, 3, 4, 12, 14, 22, 31]:    
        world.set_rule(
            world.get_entrance(f"{IDS_TO_SCENES["A10"]} to {DEVOTEE_RUNES[r]}"),
            And(
                CanReachRegion(f"{IDS_TO_SCENES["A07"]}"),
                CanReachRegion(f"{IDS_TO_SCENES["A08a"]}"),
                CanReachRegion(f"{IDS_TO_SCENES["A11"]}")
            )
        )
    # A12 DEVOTS 1, 3, 4, 5, 12, 13, 21 -- need all prior Child scenes
    for r in [1, 3, 4, 5, 12, 13, 21]:    
        world.set_rule(
            world.get_entrance(f"{IDS_TO_SCENES["A12"]} to {DEVOTEE_RUNES[r]}"),
            And(
                CanReachRegion(f"{IDS_TO_SCENES["A07"]}"),
                CanReachRegion(f"{IDS_TO_SCENES["A08a"]}"),
                CanReachRegion(f"{IDS_TO_SCENES["A10"]}"),
                CanReachRegion(f"{IDS_TO_SCENES["A11"]}")
            )
        )
    # A13 DEVOTS 7, 8, 12, 15, 21, 24 -- need Coin
    for r in [7, 8, 12, 15, 21, 24]:    
        world.set_rule(
            world.get_entrance(f"{IDS_TO_SCENES["A13"]} to {DEVOTEE_RUNES[r]}"),
            Has("Coin")
        )
    # A30 DEVOTS 1, 3, 4, 5, 10, 12, 14, 15, 17, 18, 21, 31 -- need all prior Child scenes
    for r in [1, 3, 4, 5, 10, 12, 14, 15, 17, 18, 21, 31]:    
        world.set_rule(
            world.get_entrance(f"{IDS_TO_SCENES["A30"]} to {DEVOTEE_RUNES[r]}"),
            And(
                CanReachRegion(f"{IDS_TO_SCENES["A07"]}"),
                CanReachRegion(f"{IDS_TO_SCENES["A08a"]}"),
                CanReachRegion(f"{IDS_TO_SCENES["A10"]}"),
                CanReachRegion(f"{IDS_TO_SCENES["A11"]}"),
                CanReachRegion(f"{IDS_TO_SCENES["A12"]}")
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
