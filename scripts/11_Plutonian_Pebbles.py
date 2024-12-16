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
    return len(stones)


assert num_of_stones(test_data, 25) == 55312

with open("../input_data/11_Plutonian_Pebbles.txt", "r", encoding="utf-8") as file:
    input = file.read().strip().split(" ")

answer1 = num_of_stones(input, 25)
print(answer1)


# Part 2


def num_of_stones_long(stones, blinks):
    blink_sections = []
    count = 0
    while blinks > 25:
        count += 1
        blink_sections.append(25)
        blinks = blinks - 25
    blink_sections.append(blinks)
    stone_lengths = []
    stone_sections = [stones]
    for blinks_ in blink_sections:
        tot_blinks = blinks_
        for stones_ in stone_sections:
            while blinks_:
                blinks_ = blinks_ - 1
                stones_ = blink(stones_)
            blinks_ = tot_blinks
            stone_lengths.append(len(stones_))
            stone_sections.pop(0)
            if len(stones_) != 1:
                for i in range(int(math.ceil(len(stones_) / 5))):
                    try:
                        stone_sections.append(stones_[i * 5 : (i + 1) * 5])
                    except:
                        stone_sections.append(stones_[i * 5 :])
            print(sum(stone_lengths))
        print("break")
    return sum(stone_lengths)


answer2 = num_of_stones_long(input, 75)
print(answer2)

# 15636990 too low
