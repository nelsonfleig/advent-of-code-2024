from unittest import TestCase

from days.day01.solution import part1, part2
from utils.file_reader import read_input


class TestClass(TestCase):
    def setUp(self):
        self.data = read_input("days/day01/input_test.txt")

    def test_part1(self):
        result = part1(self.data)
        self.assertEqual(result, 11)

    def test_part2(self):
        result = part2(self.data)
        self.assertEqual(result, 31)
