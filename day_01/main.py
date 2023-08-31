from part_01 import Part01
from part_02 import Part02

from common.csv_data import CSVDataManager


def main():
    csv_data_manager = CSVDataManager(is_preferred_value_str=False)
    depth_data = csv_data_manager.get_list_from_csv(file_path="measurements.csv")
    part_01 = Part01(depth_data=depth_data)

    number_of_increase = part_01()
    print(f"number_of_increase: {number_of_increase}")
    print("--- Part Two ---")
    task_02 = Part02(depth_data=depth_data)
    number_of_larger_sums = task_02()
    print(f"number_of_larger_sums: {number_of_larger_sums}")


if __name__ == "__main__":
    main()
