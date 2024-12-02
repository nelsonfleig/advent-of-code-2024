from utils.file_reader import read_input


def is_safe(reports: list[int]) -> bool:
    is_ascending = True
    is_safe = True
    for index in range(len(reports) - 1):
        curr = reports[index]
        next = reports[index + 1]
        diff = next - curr

        # on first iteration, verify if descending
        if index == 0 and diff < 0:
            is_ascending = False

        # check if there is no change or
        # change exceeds threshold of >3
        if curr == next or abs(diff) > 3:
            is_safe = False

        # check if diff direction does not change
        if (is_ascending and diff < 0) or (not is_ascending and diff > 0):
            is_safe = False

        # breakout of loop if reports not safe
        if not is_safe:
            break

    return is_safe


def part1(data: str):
    safe_total = 0
    for line in data.split("\n"):
        reports = list(map(int, line.split()))

        if is_safe(reports):
            safe_total += 1
    return safe_total


def part2(data: str):
    safe_total = 0
    for line in data.split("\n"):
        reports = list(map(int, line.split()))

        if is_safe(reports):
            safe_total += 1
        else:
            # remove one item to see if we can make reports safe
            # NOTE: This could be optimized to only remove problematic indices
            for index in range(len(reports)):
                copy = reports.copy()
                copy.pop(index)
                if is_safe(copy):
                    safe_total += 1
                    break
    return safe_total


if __name__ == "__main__":
    data = read_input("days/day02/input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
