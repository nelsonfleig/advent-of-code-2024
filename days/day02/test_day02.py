from unittest import TestCase

from days.day02.solution import part1, part2
from utils.file_reader import read_input


class TestClass(TestCase):
    def setUp(self):
        self.data = read_input("days/day02/input_test.txt")

    def test_part1(self):
        result = part1(self.data)
        self.assertEqual(result, 2)

    def test_part2(self):
        result = part2(self.data)
        self.assertEqual(result, 4)
