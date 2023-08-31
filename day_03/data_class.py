from dataclasses import dataclass, field
from typing import List, Optional


def get_last_occurrence_index(estimated_frequency: List[int], search_value: int) -> int:
    new_estimated_frequency = estimated_frequency.copy()
    new_estimated_frequency.reverse()
    reverse_index = new_estimated_frequency.index(search_value)
    last_index = len(new_estimated_frequency) - 1 - reverse_index
    return last_index


def find_the_bit(
    estimated_frequency: List[int],
    find_min_value: Optional[bool],
    find_max_value: Optional[bool],
) -> Optional[int]:

    search_bit: Optional[int] = None
    if find_min_value:
        search_bit = estimated_frequency.index(min(estimated_frequency))

    elif find_max_value:
        search_bit = get_last_occurrence_index(
            estimated_frequency, max(estimated_frequency)
        )
    return search_bit


@dataclass
class InfoOfGeneratorRating:
    """Class for keeping track of an item in inventory."""

    estimated_frequency: Optional[List[int]] = field(default=None)
    diagnosed_values: Optional[List[str]] = field(default=None)
    index: Optional[int] = field(default=None)
    searched_bit: Optional[int] = field(default=None)

    find_max_value: Optional[bool] = field(default=None)
    find_min_value: Optional[bool] = field(default=None)

    def add_info_related_with_the_index(
        self, estimated_frequency: List[int], diagnosed_values: List[str], index: int
    ):
        self.estimated_frequency = estimated_frequency
        self.diagnosed_values = diagnosed_values
        self.index = index
        self.searched_bit = find_the_bit(
            estimated_frequency=self.estimated_frequency,
            find_min_value=self.find_min_value,
            find_max_value=self.find_max_value,
        )
