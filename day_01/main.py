from common.csv_data import CSVDataManager
from part_01 import Part01
from part_02 import Part02


def main():
    csv_data_manager = CSVDataManager()
    depth_data = csv_data_manager.get_list_from_csv(file_path='measurements.csv')
    part_01 = Part01(depth_data=depth_data)

    number_of_increase = part_01()
    print(number_of_increase)
    print("--- Part Two ---")
    task_02 = Part02(depth_data=depth_data)
    number_of_increases = task_02()
    print(number_of_increases)

if __name__ == "__main__":
    main()