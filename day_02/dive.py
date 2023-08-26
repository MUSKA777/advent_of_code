from common.csv_data import CSVDataManager


class Dive:
    def __init__(self, planned_course):
        self.planned_course = planned_course

    def get_result_depth_and_horizontal_position(self):
        horizontal_position = 0
        depth = 0
        for _value in self.planned_course:
            split_value = _value.split(" ")

            if split_value[0] == "forward":
                horizontal_position += int(split_value[1])
            elif split_value[0] == "down":
                depth += int(split_value[1])
            elif split_value[0] == "up":
                depth -= int(split_value[1])

        return horizontal_position, depth

    def __call__(self, *args, **kwargs):
        horizontal_position, depth = self.get_result_depth_and_horizontal_position()
        print(f"horizontal_position: {horizontal_position}")
        print(f"depth: {depth}")
        return horizontal_position*depth
