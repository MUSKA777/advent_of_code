from typing import List, Optional

from day_03.binary_diagnostic import BinaryDiagnostic
from day_03.data_class import InfoOfGeneratorRating


class LifeSupportDiagnostic(BinaryDiagnostic):
    @staticmethod
    def evaluate_values_satisfying_the_bit_on_the_location_index(
        generator_info: InfoOfGeneratorRating,
    ) -> List[str]:
        between_grade_diagnosed_values = []
        for _value in generator_info.diagnosed_values:
            split_value = [*_value]

            if split_value[generator_info.index] == str(generator_info.searched_bit):
                between_grade_diagnosed_values.append(_value)

        return between_grade_diagnosed_values

    def get_return_the_value_satisfying_the_bits_on_the_location(
        self, generator_info: InfoOfGeneratorRating
    ) -> Optional[str]:
        diagnosed_values = self.diagnostic_report.copy()

        for index in range(len(self.diagnostic_report)):

            if len(diagnosed_values) == 1:
                break
            frequency_of_individual_bits = self.get_frequency_of_individual_bits(
                list_of_bits=diagnosed_values
            )
            estimated_frequency = frequency_of_individual_bits[index]
            generator_info.add_info_related_with_the_index(
                estimated_frequency=estimated_frequency,
                index=index,
                diagnosed_values=diagnosed_values,
            )
            diagnosed_values = (
                self.evaluate_values_satisfying_the_bit_on_the_location_index(
                    generator_info
                )
            )

        return diagnosed_values[0] if diagnosed_values else None

    def get_oxygen_generator_rating(self) -> str:
        generator_info_oxygen = InfoOfGeneratorRating(find_max_value=True)
        return self.get_return_the_value_satisfying_the_bits_on_the_location(
            generator_info=generator_info_oxygen
        )

    def get_co2_scrubber_rating(self) -> str:
        generator_info_co2 = InfoOfGeneratorRating(find_min_value=True)
        return self.get_return_the_value_satisfying_the_bits_on_the_location(
            generator_info=generator_info_co2
        )

    def __call__(self) -> int:
        oxygen_generator_rating = self.get_oxygen_generator_rating()
        co2_scrubber_rating = self.get_co2_scrubber_rating()

        return int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)
