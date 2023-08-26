
from day_02.dive import Dive
from day_02.aim import Aim
import unittest


class TestDay02(unittest.TestCase):
    planned_course = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

    def test_dive(self):
        dive = Dive(planned_course=self.planned_course)
        self.assertEqual(dive(), 150)

    def test_aim(self):
        aim = Aim(planned_course=self.planned_course)
        self.assertEqual(aim(), 900)
