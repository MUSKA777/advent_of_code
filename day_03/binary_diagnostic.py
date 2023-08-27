from typing import List


class BinaryDiagnostic:
    def __init__(self, diagnostic_report: List[str]):
        self.diagnostic_report = diagnostic_report

    @staticmethod
    def get_frequency_of_individual_bits(list_of_bits: List[str]):
        frequency_of_individual_bits: List[List[int]] = []
        for _value in list_of_bits:

            for index, bit in enumerate([*_value]):
                if index + 1 > len(frequency_of_individual_bits):
                    # 0 1
                    frequency_of_individual_bits.append([0, 0])

                if bit == "0":
                    frequency_of_individual_bits[index][0] += 1
                elif bit == "1":
                    frequency_of_individual_bits[index][1] += 1
        return frequency_of_individual_bits

    def get_gamma_rate_binary(self) -> str:
        frequency_of_individual_bits = self.get_frequency_of_individual_bits(
            list_of_bits=self.diagnostic_report
        )
        gama_rate_binary = ""
        for frequency in frequency_of_individual_bits:
            max_index = frequency.index(max(frequency))
            gama_rate_binary += str(max_index)
        return gama_rate_binary

    @staticmethod
    def get_epsilon_rate_binary(gama_rate_binary: str) -> str:
        epsilon_rate_binary = ""
        for bit in gama_rate_binary:
            if bit == "0":
                epsilon_rate_binary += "1"
            elif bit == "1":
                epsilon_rate_binary += "0"
        return epsilon_rate_binary

    def __call__(self) -> int:
        gama_rate_binary = self.get_gamma_rate_binary()
        epsilon_rate_binary = self.get_epsilon_rate_binary(
            gama_rate_binary=gama_rate_binary
        )
        return int(gama_rate_binary, 2) * int(epsilon_rate_binary, 2)
