# Day 9 - Disk Fragmenter

test_data1 = "12345"
test_answer1 = 60

test_data2 = "2333133121414131402"
test_answer2 = 1928
test_answer2_2 = 2858


def parse_data(input):
    input_list = [char for char in input]
    parsed = []
    for num, point in enumerate(input_list):
        if num % 2:
            parsed.extend(["."] * int(point))
        else:
            parsed.extend([int(num / 2)] * int(point))
    return parsed


assert parse_data(test_data1) == [
    0,
    ".",
    ".",
    1,
    1,
    1,
    ".",
    ".",
    ".",
    ".",
    2,
    2,
    2,
    2,
    2,
]


def move_files(parsed):
    while type(parsed[-1]) == int:
        try:
            first_empty = parsed.index(".")
        except:
            break
        parsed[first_empty] = parsed[-1]
        parsed.pop()
        while parsed[-1] == ".":
            parsed.pop()
    return parsed


parsed1 = parse_data(test_data1)
assert move_files(parsed1) == [0, 2, 2, 1, 1, 1, 2, 2, 2]


def compute_checksum(input):
    parsed = parse_data(input)
    reordered = move_files(parsed)
    checksum = 0
    for index, file in enumerate(reordered):
        if type(file) == int:
            checksum += index * file
    return checksum


assert compute_checksum(test_data1) == test_answer1
assert compute_checksum(test_data2) == test_answer2

with open("../input_data/09_Disk_Fragmenter.txt", "r", encoding="utf-8") as file:
    input = file.read().strip().split("\n")

input = "".join(line for line in input)

answer1 = compute_checksum(input)
print(answer1)
