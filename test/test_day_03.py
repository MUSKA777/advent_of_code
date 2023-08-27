from day_03.life_support_diagnostic import LifeSupportDiagnostic
from day_03.binary_diagnostic import BinaryDiagnostic
import unittest


class TestDay02(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestDay02, self).__init__(*args, **kwargs)
        self.diagnostic_report = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100",
                                  "10000", "11001", "00010", "01010"]
        self.binary_diagnostic = BinaryDiagnostic(diagnostic_report=self.diagnostic_report)
        self.life_support_rating = LifeSupportDiagnostic(diagnostic_report=self.diagnostic_report)

    def test_get_gamma_rate_binary(self):
        self.assertEqual("10110", self.binary_diagnostic.get_gamma_rate_binary())

    def test_get_epsilon_rate_binary(self):
        self.assertEqual("01001", self.binary_diagnostic.get_epsilon_rate_binary(gama_rate_binary="10110"))

    def test_binary_diagnostic(self):
        self.assertEqual(198, self.binary_diagnostic())

    def test_get_oxygen_generator_number(self):
        self.assertEqual("10111", self.life_support_rating.get_oxygen_generator_number())

    def test_get_co2_scrubber_rating(self):
        self.assertEqual("01010", self.life_support_rating.get_co2_scrubber_rating())

    def test_life_support_rating(self):
        self.assertEqual(230, self.life_support_rating())
