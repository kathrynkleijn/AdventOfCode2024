# Day 3 - Mull It Over
import re

test_data = (
    """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
)

test_answer = 161


def find_real_instructions(input):
    return re.findall("mul\(\d+,\d+\)", input)


assert find_real_instructions(test_data) == [
    "mul(2,4)",
    "mul(5,5)",
    "mul(11,8)",
    "mul(8,5)",
]


def decode_instructions(instructions):
    mul = 0
    for instruction in instructions:
        numbers = [int(num) for num in re.findall("\d+", instruction)]
        mul += numbers[0] * numbers[1]
    return mul


assert decode_instructions(["mul(1,2)", "mul(44,46)", "mul(123,4)"]) == 2518

assert (
    decode_instructions(
        [
            "mul(2,4)",
            "mul(5,5)",
            "mul(11,8)",
            "mul(8,5)",
        ]
    )
    == test_answer
)

with open("../input_data/03_Mull_It_Over.txt", "r", encoding="utf-8") as file:
    input = file.read().strip()

instructions = find_real_instructions(input)
answer_1 = decode_instructions(instructions)
print(answer_1)
