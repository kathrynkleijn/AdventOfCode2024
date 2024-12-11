# Day 9 - Disk Fragmenter

from collections import OrderedDict

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

# answer1 = compute_checksum(input)
# print(answer1)


# Part 2


def parse_data(input):
    input_list = [char for char in input]
    files = OrderedDict()
    free = OrderedDict()
    index = 0
    for num, point in enumerate(input_list):
        if num % 2:
            free[index] = int(point)
        else:
            files[int(num / 2)] = [index, int(point)]
        index += int(point)

    return files, free


assert parse_data(test_data1) == (
    {0: [0, 1], 1: [3, 3], 2: [10, 5]},
    {1: 2, 6: 4},
)


def files_repr(files, free):
    parsed = []
    reordered_files = OrderedDict()
    for id, value in files.items():
        reordered_files[value[0]] = [id, value[1]]
    reordered_files = OrderedDict(sorted(reordered_files.items()))
    free = OrderedDict(sorted(free.items()))
    for value in reordered_files.values():
        parsed.extend([value[0]] * value[1])
    for index, empty in free.items():
        for i in range(empty):
            parsed.insert(index + i, ".")
    return parsed


def move_files(files, free):
    for key, value in reversed(files.items()):

        for i in range(len(list(free.values()))):
            empty_length = list(free.values())[i]
            empty_place = list(free.keys())[i]

            if value[1] <= empty_length and value[0] > empty_place:
                files[key] = [empty_place, value[1]]
                remaining_free = empty_length - value[1]
                new_index = empty_place + value[1]
                del free[empty_place]
                if remaining_free:
                    free[new_index] = remaining_free
                    free = OrderedDict(sorted(free.items()))
                free[value[0]] = value[1]

                break
            else:
                continue

    return files, free


def move_files2(files, free):
    for key, value in reversed(files.items()):
        empty_list = list(free.items())
        possible_space = [
            (x, y) for (x, y) in empty_list if y >= value[1] and x < value[0]
        ]
        try:
            index = empty_list.index(possible_space[0])

            empty_length = list(free.values())[index]
            empty_place = list(free.keys())[index]

            files[key] = [empty_place, value[1]]
            remaining_free = empty_length - value[1]
            new_index = empty_place + value[1]
            del free[empty_place]
            if remaining_free:
                free[new_index] = remaining_free
            free[value[0]] = value[1]
            free = OrderedDict(sorted(free.items()))
        except:
            continue

    return files, free


files1, free1 = parse_data(test_data1)
assert files_repr(files1, free1) == [
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


def compute_checksum(input):
    files, free = parse_data(input)
    reordered_files, free = move_files(files, free)
    checksum = 0
    for id, value in reordered_files.items():
        for i in range(value[1]):
            checksum += id * (value[0] + i)
    return checksum


assert compute_checksum(test_data2) == test_answer2_2


def compute_checksum2(input):
    files, free = parse_data(input)
    reordered_files, free = move_files2(files, free)
    checksum = 0
    for id, value in reordered_files.items():
        for i in range(value[1]):
            checksum += id * (value[0] + i)
    return checksum


assert compute_checksum2(test_data2) == test_answer2_2

answer2 = compute_checksum2(input)
print(answer2)
