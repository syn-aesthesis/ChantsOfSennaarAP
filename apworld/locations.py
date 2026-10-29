from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification, Location
from . import items
if TYPE_CHECKING:
    from .world import ChantsOfSennaarWorld


LOCATION_NAME_TO_ID = {
    "Observe Devotee Rune 10": 110,
    "Observe Devotee Rune 11": 111,
    "Observe Devotee Rune 19": 119,
    "Complete Devotee Journal Page 01": 501,
}

REGION_NAMES = [
    "Crypt Spawn",
    "Crypt Stairway",
    "Crypt Sewer Gate",
    "Crypt Valves",
    "Crypt Sewer Viaduct",
    "Devotee Rune 10",
    "Devotee Rune 11",
    "Devotee Rune 19",
    "Devotee Journal Page 01",
]


class ChantsOfSennaarLocation(Location):
    game = "Chants of Sennaar"


def get_location_names_with_ids(location_names: list[str]):
    return {location_name: LOCATION_NAME_TO_ID[location_name] 
            for location_name in location_names}


def create_all_locations(world: ChantsOfSennaarWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: ChantsOfSennaarWorld) -> None:
    regions: dict[str, Region] = {}
    for region_name in REGION_NAMES:
        regions[region_name] = world.get_region(region_name)

    rune_locations: dict[str, list[str]] = {
        "Devotee Rune 10": ["Observe Devotee Rune 10"],
        "Devotee Rune 11": ["Observe Devotee Rune 11"],
        "Devotee Rune 19": ["Observe Devotee Rune 19"],
    }

    page_locations: dict[str, list[str]] = {
        "Devotee Journal Page 01": ["Complete Devotee Journal Page 01"],
    }

    region_locations = rune_locations | page_locations

    for region_name, location_names in region_locations.items():
        regions[region_name].add_locations(get_location_names_with_ids(
                                           location_names), 
                                           ChantsOfSennaarLocation)


def create_events(world: ChantsOfSennaarWorld) -> None:
    goal_region = world.get_region("Devotee Journal Page 01")
    goal_region.add_event("Goal Condition", "Goal", 
                          location_type=ChantsOfSennaarLocation,
                          item_type=items.ChantsOfSennaarItem)
