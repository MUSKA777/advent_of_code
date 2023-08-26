from typing import List
from common.csv_data import CSVDataManager


class Part01:

    def __init__(self, depth_data: List[int]):
        self.depth_data = depth_data

    def get_the_depth_increases(self) -> List[int]:
        depth_increases: List[int] = []
        for index, depth in enumerate(self.depth_data):
            if index == 0:
                continue
            depth_increases.append(depth - self.depth_data[index - 1])
        return depth_increases

    @staticmethod
    def get_the_number_of_times_a_depth_measurement_increases(depth_increases: List[int]) -> int:
        number_of_increase: int = 0
        for increase in depth_increases:
            if increase > 0:
                number_of_increase += 1
        return number_of_increase

    def __call__(self) -> int:
        depth_increases = self.get_the_depth_increases()
        return self.get_the_number_of_times_a_depth_measurement_increases(depth_increases=depth_increases)


