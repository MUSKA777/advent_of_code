from common.csv_data import CSVDataManager
from binary_diagnostic import BinaryDiagnostic
from life_support_diagnostic import LifeSupportDiagnostic

def main():
    csv_data_manager = CSVDataManager(is_preferred_value_str=True)
    diagnostic_report = csv_data_manager.get_list_from_csv(file_path='measurements_03.csv')
    binary_diagnostic = BinaryDiagnostic(diagnostic_report=diagnostic_report)
    power_consumption = binary_diagnostic()
    print(f"power_consumption: {power_consumption}")
    life_support_diagnostic = LifeSupportDiagnostic(diagnostic_report=diagnostic_report)
    rating_of_life_support = life_support_diagnostic()
    print(f"rating_of_life_support: {rating_of_life_support}")


if __name__ == "__main__":
    main()
