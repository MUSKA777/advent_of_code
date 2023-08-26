from typing import List, Tuple


class Part02:
    def __init__(self, depth_data: List[int]):
        self.depth_data = depth_data

    def get_all_sums_three_measurement_sliding_window(self) -> List[int]:
        all_sums_three_measurement_sliding_window = []
        for index, _value in enumerate(self.depth_data):
            if len(self.depth_data) < index+1+2:
                break
            sliding_window = [_value, self.depth_data[index+1], self.depth_data[index+2]]
            all_sums_three_measurement_sliding_window.append(sum(sliding_window))
        return all_sums_three_measurement_sliding_window

    @staticmethod
    def get_data_comparison(all_sums: List[int]) -> Tuple[List[str], int]:
        data_comparison = []
        number_of_increases = 0
        for index, _sum in enumerate(all_sums):
            if index == 0:
                continue
            if _sum > all_sums[index-1]:
                data_comparison.append("increased")
                number_of_increases += 1
            elif _sum == all_sums[index-1]:
                data_comparison.append("no change")
            elif _sum < all_sums[index-1]:
                data_comparison.append("decreased")
        return data_comparison, number_of_increases

    def __call__(self):
        all_sums = self.get_all_sums_three_measurement_sliding_window()
        [data_comparison, number_of_increases] = self.get_data_comparison(all_sums=all_sums)
        print(data_comparison)
        return number_of_increases








