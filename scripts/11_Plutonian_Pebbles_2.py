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

single_digits = {}
for i in range(10):
    answer = num_of_stones([str(i)], 25)
    single_digits[str(i)] = answer
multiples_of_2024 = {}
for i in range(1, 10):
    answer = num_of_stones([str(i * 2024)], 25)
    multiples_of_2024[str(i * 2024)] = answer
multiples_split = {}
for i in range(1, 5):
    answer = num_of_stones([str(i * 20)], 25)
    multiples_split[str(i * 20)] = answer
    answer = num_of_stones([str(i * 24)], 25)
    multiples_split[str(i * 24)] = answer


def num_stones_75_blinks(starting_stones, init=False):
    stone_lengths = 0
    if not init:
        for stone in starting_stones:
            if stone == "0":
                stone_lengths += zero_full
        starting_stones = [stone for stone in starting_stones if stone != "0"]
    length, stones_1 = num_of_stones(starting_stones, 25)
    stone_lengths += length
    print(stone_lengths)
    print(f"sections = {len(stones_1)}")
    updated_sections = []
    for stone in stones_1:
        if stone in range(10):
            length, stones_ = single_digits[stone]
        elif stone in multiples_of_2024.keys():
            length, stones = multiples_of_2024[stone]
        elif stone in multiples_split.keys():
            length, stones_ = multiples_split[stone]
        else:
            length, stones_ = num_of_stones(stone, 25)
        stone_lengths += length
        print(stone_lengths)
        updated_sections.append(stones_)
    for stones in updated_sections:
        print(f"sections = {len(stones)}")
        for stone in stones:
            if stone in range(10):
                length = single_digits[stone][0]
            elif stone in multiples_of_2024.keys():
                length = multiples_of_2024[stone][0]
            elif stone in multiples_split.keys():
                length = multiples_split[stone][0]
            else:
                length = num_of_stones(stone, 25)[0]
            stone_lengths += length
            print(stone_lengths)
    return stone_lengths


# zero_full = num_stones_75_blinks(["0"], init=True)


# answer2 = num_stones_75_blinks(input)
# print(answer2)

# 15636990 too low
