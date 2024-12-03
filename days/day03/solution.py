import re

from utils.file_reader import read_input


def part1(data: str):
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)
    total = 0
    for match in matches:
        a, b = list(map(lambda x: re.sub(r"\D+", "", x), match.split(",")))
        total += int(a) * int(b)
    return total


def part2(data: str):
    joined = re.sub(r"\n", "", data)
    cleaned = re.sub(r"don't\(\).+?do\(\)", "", joined)

    # check if there is a straggling "don't" and remove it
    last_dont_idx = cleaned.find("don't")
    if last_dont_idx != -1:
        cleaned = cleaned[:last_dont_idx]

    return part1(cleaned)


if __name__ == "__main__":
    data = read_input("days/day03/input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
