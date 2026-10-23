from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Entrance, Region
if TYPE_CHECKING:
    from .world import ChantsOfSennaarWorld

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

def create_and_connect_regions(world: ChantsOfSennaarWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: ChantsOfSennaarWorld) -> None:
    regions: list[Region] = []
    for region_name in REGION_NAMES:
        regions.append(Region(region_name, world.player, world.multiworld))

    world.multiworld.regions += regions


def connect_regions(world: ChantsOfSennaarWorld) -> None:
    regions: dict[str, Region] = {}
    for region_name in REGION_NAMES:
        regions[region_name] = world.get_region(region_name)

    # define Entrance connections between physical regions
    regions["Crypt Spawn"].connect(regions["Crypt Stairway"], "Crypt Spawn exit")
    regions["Crypt Stairway"].connect(regions["Crypt Sewer Gate"], "Crypt Stairway exit")
    regions["Crypt Sewer Gate"].connect(regions["Crypt Valves"], "Crypt Sewer Gate exit")
    regions["Crypt Valves"].connect(regions["Crypt Sewer Viaduct"], "Crypt Valves exit")

    # define Entrance connections to rune regions
    regions["Crypt Sewer Gate"].connect(regions["Devotee Rune 10"], "Crypt Sewer Gate rune A10")
    regions["Crypt Sewer Gate"].connect(regions["Devotee Rune 11"], "Crypt Sewer Gate rune A11")
    regions["Crypt Sewer Gate"].connect(regions["Devotee Rune 19"], "Crypt Sewer Gate rune A19")
    regions["Crypt Valves"].connect(regions["Devotee Rune 10"], "Crypt Valves rune A10")
    regions["Crypt Valves"].connect(regions["Devotee Rune 11"], "Crypt Valves rune A11")

    # define Entrance connections to journal regions
    regions["Crypt Valves"].connect(regions["Devotee Journal Page 01"], "Crypt Valves journal A01")