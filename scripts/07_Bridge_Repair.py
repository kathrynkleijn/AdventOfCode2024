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
ops = [sum, math.prod]


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


def check_simple(key, value):
    for op in ops:
        if op([int(val) for val in value]) == int(key):
            return int(key)
    return False


assert check_simple("190", ["10", "19"]) == 190


def check_permutations(key, value):
    num_operators = len(value) - 1
    for perm in itertools.permutations(ops, num_operators):
        layer = perm[0](([int(value[0]), int(value[1])]))
        for i in range(1, num_operators):
            layer = perm[i]([layer, int(value[i + 1])])
        if layer == int(key):
            return int(key)

    return False


assert check_permutations("190", ["10", "19"]) == 190
assert check_permutations("3267", ["81", "40", "27"]) == 3267


def find_calibration_possibilities(input):
    total_cal = 0
    for key, value in input.items():
        simple = check_simple(key, value)
        if simple:
            total_cal += 0
            continue
        else:
            pass
    return total_cal
