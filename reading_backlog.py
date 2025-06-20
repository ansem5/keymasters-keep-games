from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class ReadingBacklogArchipelagoOptions:
    reading_backlog_game_selection: ReadingBacklogBookSelection
    reading_backlog_actions: ReadingBacklogActions


class ReadingBacklogGame(Game):
    name = "Reading Backlog"
    platform = KeymastersKeepGamePlatforms.META

    platforms_other = None

    is_adult_only_or_unrated = False

    options_cls = ReadingBacklogArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[Game ObjectiveTemplate]:
        return [
            ReadingObjectiveTemplate(
                label="ACTION BOOK",
                data={"ACTION": (self.actions, 1), "BOOK": (self.books, 1)},
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
        ]

    def actions(self) -> List[str]:
        return sorted(self.archipelago_options.reading_backlog_actions.value)

    def games(self) -> List[str]:
        return sorted(self.archipelago_options.reading_backlog_game_selection.value)


# Archipelago Options
class ReadingBacklogBookSelection(OptionSet):
    """
    Defines which books are in the player's backlog.

    Replace the placeholders with values of your own choosing.
    """

    display_name = "Reading Backlog Book Selection"

    default = ["Book 1", "Book 2", "..."]


class ReadingBacklogActions(OptionSet):
    """
    Defines the possible actions that could be required on a book in the backlog.

    You can customize this list to your liking.
    """

    display_name = "Reading Backlog Actions"

    default = [
        "READ",
        "FINISH",
    ]
