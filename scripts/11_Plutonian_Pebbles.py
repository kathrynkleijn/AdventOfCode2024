# Day 11 - Plutonian Pebbles

import math

test_data = "125 17".split(" ")
test_data2 = "0 1 10 99 999".split(" ")


def blink(stones):
    updated_stones = []
    for stone in stones:
        if stone == "0":
            updated_stones.append("1")
        elif not len(stone) % 2:
            first_stone = str(int(stone[: int((len(stone) / 2))]))
            second_stone = str(int(stone[int(len(stone) / 2) :]))
            updated_stones.extend([first_stone, second_stone])
        else:
            updated_stones.append(str(int(stone) * 2024))
    return updated_stones


assert blink(test_data) == ["253000", "1", "7"]
assert blink(test_data2) == ["1", "2024", "1", "0", "9", "9", "2021976"]


def num_of_stones(stones, blinks):
    while blinks:
        blinks = blinks - 1
        stones = blink(stones)
    return len(stones), stones


assert num_of_stones(test_data, 25)[0] == 55312

with open("../input_data/11_Plutonian_Pebbles.txt", "r", encoding="utf-8") as file:
    input = file.read().strip().split(" ")

answer1 = num_of_stones(input, 25)[0]
print(answer1)


# Part 2

zero_answer = num_of_stones(["0"], 25)
one_answer = num_of_stones(["1"], 25)

stone_lengths, stones_1 = num_of_stones(input, 25)
print(stone_lengths)
print(f"sections = {len(stones_1)}")
updated_sections = []
for num, stone in enumerate(stones_1):
    if stone == "0":
        length, stones_ = zero_answer
    elif stone == "1":
        length, stones_ = one_answer
    else:
        length, stones_ = num_of_stones(stone, 25)
    stone_lengths += length
    print(num, stone_lengths)
    updated_sections.append(stones_)
for stones in updated_sections:
    print(f"sections = {len(stones)}")
    for stone in stones:
        if stone == "0":
            length = zero_answer[0]
        elif stone == "1":
            length = one_answer[0]
        else:
            length = num_of_stones(stone, 25)[0]
        stone_lengths += length
        print(stone_lengths)


answer2 = stone_lengths
print(answer2)

# 15636990 too low
