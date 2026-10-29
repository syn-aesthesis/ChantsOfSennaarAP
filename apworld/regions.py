from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Entrance, Region
if TYPE_CHECKING:
    from .world import ChantsOfSennaarWorld

from .cos_data import *


def create_and_connect_regions(world: ChantsOfSennaarWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: ChantsOfSennaarWorld) -> None:
    regions: list[Region] = []
    for region_name in ALL_REGIONS:
        regions.append(Region(region_name, world.player, world.multiworld))

    world.multiworld.regions += regions


def connect_regions(world: ChantsOfSennaarWorld) -> None:
    regions: dict[str, Region] = {}
    for region_name in ALL_REGIONS:
        regions[region_name] = world.get_region(region_name)

    # define Entrance connections between scene regions
    for src_id, dst_ids in ABBEY_SCENE_ENTRANCES.items():
        src_scene = ABBEY_IDS_TO_SCENES[src_id]
        
        for dst_id in dst_ids:
            dst_scene = ABBEY_IDS_TO_SCENES[dst_id]
            regions[src_scene].connect(regions[dst_scene], 
                                       f"{src_scene} to {dst_scene}")

    # define Entrance connections to rune regions
    for src_id, lang_runes in ABBEY_RUNE_ENTRANCES.items():
        src_scene = ABBEY_IDS_TO_SCENES[src_id]

        for lang, rune_ids in lang_runes:
            for r in rune_ids:
                dst_rune = f"{lang} Rune {r+1:02d}"
                regions[src_scene].connect(regions[dst_rune], 
                                           f"{src_scene} to {dst_rune}")

    # define Entrance connections to journal regions
    for page_name in DEVOTEE_PAGES:
        origin = world.origin_region_name
        regions[origin].connect(regions[page_name], 
                                f"{world.origin_region_name} to {page_name}")
