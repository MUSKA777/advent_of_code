import unittest
from day_01.part_01 import Part01
from day_01.part_02 import Part02


class TestDay01(unittest.TestCase):
    depth_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    def test_part_01(self):
        part_01 = Part01(depth_data=self.depth_data)
        self.assertEqual(part_01(), 7)

    def test_part_02(self):
        part_02 = Part02(depth_data=self.depth_data)
        self.assertEqual(part_02(), 5)




