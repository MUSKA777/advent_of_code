import csv

class CSVDataManager:
    def __init__(self, is_preferred_value_str: bool = True):
        self.is_preferred_value_str = is_preferred_value_str

    def convert_possible_value_to_int(self, value):
        try:
            if int(value):
                return int(value)
        except Exception:
            return value

    def get_list_from_csv(self, file_path):
        all_data = []
        with open(file_path, mode='r') as file:
            # reading the CSV file
            csvFile = csv.reader(file)

            # displaying the contents of the CSV file
            for lines in csvFile:
                for _value in lines:
                    if self.is_preferred_value_str:
                        all_data.append(_value)
                        continue
                    all_data.append(self.convert_possible_value_to_int(_value))

        return all_data


