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


# Part 2

test_data2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
test_answer2 = 48


def split_on_conditionals(input):
    do_sections = []
    sections = input.split("do()")
    for section in sections:
        dont_sections = section.split("don't()")
        do_sections.append(dont_sections[0])
    return do_sections


assert split_on_conditionals(test_data2) == ["xmul(2,4)&mul[3,7]!^", "?mul(8,5))"]


def decode_with_conditionals(input):
    do_sections = split_on_conditionals(input)
    mul = 0
    for section in do_sections:
        instructions = find_real_instructions(section)
        mul += decode_instructions(instructions)
    return mul


assert decode_with_conditionals(test_data2) == test_answer2


answer_2 = decode_with_conditionals(input)
print(answer_2)
