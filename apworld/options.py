from dataclasses import dataclass
from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle


class GoalType(Choice):
    """
    Defines the goal condition.
    """

    display_name = "Goal Type"

    option_true_ending = 0
    option_any_ending = 1
    option_journal_hunt = 2

    default = option_journal_hunt


class JournalHuntPageCount(Range):
    """
    If journal_hunt is chosen as the goal type,
    defines the number of complete journal pages needed to goal.
    """

    display_name = "Journal Hunt Page Count"

    range_start = 1
    range_end = 55

    default = 1


class TrapChance(Range):
    """
    Percent chance that any given filler item will be replaced by a trap item.
    """

    display_name = "Trap Chance"

    range_start = 0
    range_end = 100
    default = 0


@dataclass
class ChantsOfSennaarOptions(PerGameCommonOptions):
    goal_type: GoalType
    journal_hunt_page_count: JournalHuntPageCount
    trap_chance: TrapChance
