from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification, Location
from . import items
if TYPE_CHECKING:
    from .world import ChantsOfSennaarWorld

from .cos_data import *


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
    for region_name in ALL_REGIONS:
        regions[region_name] = world.get_region(region_name)

    rune_locations: dict[str, list[str]] = {
        rune: [f"Observe {rune}"] for rune in RUNE_REGIONS
    }

    page_locations: dict[str, list[str]] = {
        page: [f"Complete {page}"] for page in PAGE_REGIONS
    }

    region_locations = rune_locations | page_locations

    for region_name, location_names in region_locations.items():
        regions[region_name].add_locations(
            get_location_names_with_ids(location_names), 
            ChantsOfSennaarLocation
        )


def create_events(world: ChantsOfSennaarWorld) -> None:
    goal_region = world.get_region("Devotee Journal Page 01")
    goal_region.add_event("Goal Condition", "Goal", 
                          location_type=ChantsOfSennaarLocation,
                          item_type=items.ChantsOfSennaarItem)
