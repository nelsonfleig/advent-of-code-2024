from utils.file_reader import read_input


def split_lists(data: str) -> tuple[list[int], list[int]]:
    left = []
    right = []
    for line in data.split("\n"):
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()
    return left, right


def part1(data: str):
    distance = 0
    left, right = split_lists(data)
    for i in range(len(left)):
        distance += abs(left[i] - right[i])
    return distance


def part2(data: str):
    similarity = 0
    left, right = split_lists(data)
    left_dict = dict.fromkeys(left, 0)
    for num in right:
        if num in left_dict:
            left_dict[num] += 1
    for num in left:
        similarity += num * left_dict[num]
    return similarity


if __name__ == "__main__":
    data = read_input("days/day01/input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
