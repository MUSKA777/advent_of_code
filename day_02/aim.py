

class Aim:
    def __init__(self, planned_course):
        self.planned_course = planned_course

    def get_aim(self):
        horizontal_position = 0
        depth = 0
        aim = 0
        for _value in self.planned_course:
            split_value = _value.split(" ")

            if split_value[0] == "forward":
                horizontal_position += int(split_value[1])
                depth += (aim*int(split_value[1]))

            elif split_value[0] == "down":
                aim += int(split_value[1])

            elif split_value[0] == "up":
                aim -= int(split_value[1])
        print(f"horizontal_position: {horizontal_position}")
        print(f"depth: {depth}")
        print(f"aim: {aim}")
        return horizontal_position, depth

    def __call__(self, *args, **kwargs):
        horizontal_position, depth = self.get_aim()
        return horizontal_position*depth

