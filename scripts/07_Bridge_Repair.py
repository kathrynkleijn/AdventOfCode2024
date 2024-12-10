# Day 7 - Bridge Repair
from operator import add, mul
import math
import itertools


test_data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".split(
    "\n"
)

test_answer = 3749
test_answer2 = 11387


def concatentaion(values):
    return int(str(values[0]) + str(values[1]))


assert concatentaion([15, 6]) == 156

ops_1 = [sum, math.prod]
ops_2 = [sum, math.prod, concatentaion]


def parse_data(input):
    parsed_dict = {}
    for line in input:
        parsed_dict[line.split(":")[0]] = line.split(":")[1].split()
    return parsed_dict


test_data_short = """190: 10 19
3267: 81 40 27""".split(
    "\n"
)

assert parse_data(test_data_short) == {"190": ["10", "19"], "3267": ["81", "40", "27"]}


def check_permutations(key, value, ops):
    num_operators = len(value) - 1
    for perm in itertools.product(ops, repeat=num_operators):
        layer = perm[0](([int(value[0]), int(value[1])]))
        for i in range(1, num_operators):
            layer = perm[i]([layer, int(value[i + 1])])
        if layer == int(key):
            return int(key)

    return False


assert check_permutations("190", ["10", "19"], ops_1) == 190
assert check_permutations("3267", ["81", "40", "27"], ops_1) == 3267
assert check_permutations("292", ["11", "6", "16", "20"], ops_1) == 292


def find_calibration_possibilities(input, ops):
    total_cal = 0
    for key, value in input.items():
        total_cal += check_permutations(key, value, ops)
    return total_cal


test_parsed = parse_data(test_data)
assert find_calibration_possibilities(test_parsed, ops_1) == test_answer
assert find_calibration_possibilities(test_parsed, ops_2) == test_answer2

if __name__ == "__main__":
    with open("../input_data/07_Bridge_Repair.txt", "r", encoding="utf-8") as file:
        input = file.read().strip().split("\n")

    parsed = parse_data(input)
    answer1 = find_calibration_possibilities(parsed, ops_1)
    print(answer1)

    answer2 = find_calibration_possibilities(parsed, ops_2)
    print(answer2)
