from day_03.binary_diagnostic import BinaryDiagnostic
from typing import List

class LifeSupportDiagnostic(BinaryDiagnostic):

    def get_last_occurrence_index(self, estimated_frequency: List[int], search_value: int) -> int:
        new_estimated_frequency = estimated_frequency.copy()
        new_estimated_frequency.reverse()
        reverse_index = new_estimated_frequency.index(search_value)
        last_index = len(new_estimated_frequency) - 1 - reverse_index
        return last_index


    def get_generator_number(self, find_max_value: bool=True, find_min_value:bool = False):
        diagnosed_values = self.diagnostic_report.copy()

        for index in range(len(self.diagnostic_report)):
            between_grade_diagnosed_values = []
            if len(diagnosed_values) == 1:
                break
            frequency_of_individual_bits = self.get_frequency_of_individual_bits(list_of_bits=diagnosed_values)

            for _value in diagnosed_values.copy():
                split_value = [*_value]
                estimated_frequency = frequency_of_individual_bits[index]

                if find_min_value:
                    last_occurrence_index = estimated_frequency.index(min(estimated_frequency))

                elif find_max_value:
                    last_occurrence_index = self.get_last_occurrence_index(estimated_frequency, max(estimated_frequency))

                else:
                    raise Exception

                if split_value[index] == str(last_occurrence_index):
                    between_grade_diagnosed_values.append(_value)

            diagnosed_values = between_grade_diagnosed_values.copy()
        return diagnosed_values

    def get_oxygen_generator_number(self):
        diagnosed_values = self.get_generator_number(find_max_value=True)

        return diagnosed_values[0] if diagnosed_values else None

    def get_co2_scrubber_rating(self):
        diagnosed_values = self.get_generator_number(find_min_value=True)

        return diagnosed_values[0] if diagnosed_values else None

    def __call__(self, *args, **kwargs):
        oxygen_generator_number = self.get_oxygen_generator_number()
        co2_scrubber_rating = self.get_co2_scrubber_rating()
        return int(oxygen_generator_number, 2) * int(co2_scrubber_rating, 2)







