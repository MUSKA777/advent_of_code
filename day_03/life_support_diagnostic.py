from typing import List, Optional

from day_03.binary_diagnostic import BinaryDiagnostic


class LifeSupportDiagnostic(BinaryDiagnostic):
    @staticmethod
    def get_last_occurrence_index(
        estimated_frequency: List[int], search_value: int
    ) -> int:
        new_estimated_frequency = estimated_frequency.copy()
        new_estimated_frequency.reverse()
        reverse_index = new_estimated_frequency.index(search_value)
        last_index = len(new_estimated_frequency) - 1 - reverse_index
        return last_index

    def get_generator_rating(
        self, find_max_value: bool = True, find_min_value: bool = False
    ) -> Optional[str]:
        diagnosed_values = self.diagnostic_report.copy()

        for index in range(len(self.diagnostic_report)):
            between_grade_diagnosed_values = []
            if len(diagnosed_values) == 1:
                break
            frequency_of_individual_bits = self.get_frequency_of_individual_bits(
                list_of_bits=diagnosed_values
            )

            for _value in diagnosed_values.copy():
                split_value = [*_value]
                estimated_frequency = frequency_of_individual_bits[index]

                if find_min_value:
                    last_occurrence_index = estimated_frequency.index(
                        min(estimated_frequency)
                    )

                elif find_max_value:
                    last_occurrence_index = self.get_last_occurrence_index(
                        estimated_frequency, max(estimated_frequency)
                    )

                else:
                    raise Exception

                if split_value[index] == str(last_occurrence_index):
                    between_grade_diagnosed_values.append(_value)

            diagnosed_values = between_grade_diagnosed_values.copy()
        return diagnosed_values[0] if diagnosed_values else None

    def __call__(self, *args, **kwargs) -> int:
        oxygen_generator_rating = self.get_generator_rating(find_max_value=True)
        co2_scrubber_rating = self.get_generator_rating(find_min_value=True)
        return int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)
