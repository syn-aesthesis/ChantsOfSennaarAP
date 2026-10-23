from __future__ import annotations
from typing import TYPE_CHECKING
from rule_builder.rules import Has, HasAll, CanReachLocation, Rule
if TYPE_CHECKING:
    from .world import ChantsOfSennaarWorld


def set_all_rules(world: ChantsOfSennaarWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: ChantsOfSennaarWorld) -> None:
    crypt_valves_exit = world.get_entrance("Crypt Valves exit")
    journal_a01_check = world.get_entrance("Crypt Valves journal A01")
    can_complete_journal_a01 = HasAll("Devotee Rune 10", "Devotee Rune 11", "Devotee Rune 19")
    world.set_rule(crypt_valves_exit, can_complete_journal_a01)
    world.set_rule(journal_a01_check, can_complete_journal_a01)


def set_all_location_rules(world: ChantsOfSennaarWorld) -> None:
    goal_location = world.get_location("Goal Condition")
    can_reach_goal = CanReachLocation("Complete Devotee Journal Page 01")
    world.set_rule(goal_location, can_reach_goal)


def set_completion_condition(world: ChantsOfSennaarWorld) -> None:
    world.set_completion_rule(Has("Goal"))