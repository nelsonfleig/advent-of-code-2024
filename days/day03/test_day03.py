from unittest import TestCase

from days.day03.solution import part1, part2
from utils.file_reader import read_input


class TestClass(TestCase):
    def test_part1(self):
        data = read_input("days/day03/input_test.txt")
        result = part1(data)
        self.assertEqual(result, 161)

    def test_part2_sample(self):
        data = read_input("days/day03/input_test_part2a.txt")
        result = part2(data)
        self.assertEqual(result, 48)

    def test_part2_ends_with_dont(self):
        data = read_input("days/day03/input_test_part2b.txt")
        result = part2(data)
        self.assertEqual(result, 48)

    def test_part2_with_line_break(self):
        data = read_input("days/day03/input_test_part2c.txt")
        result = part2(data)
        self.assertEqual(result, 88)
