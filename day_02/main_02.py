from common.csv_data import CSVDataManager
from dive import Dive
from aim import Aim


def main():
    csv_data_manager = CSVDataManager()
    planned_course = csv_data_manager.get_list_from_csv(file_path='measurements_02.csv')
    dive = Dive(planned_course=planned_course)
    print(f"dive: {dive()}")
    print("--- Part Two ---")
    aim = Aim(planned_course=planned_course)
    print(f"aim: {aim()}")


if __name__ == "__main__":
    main()
