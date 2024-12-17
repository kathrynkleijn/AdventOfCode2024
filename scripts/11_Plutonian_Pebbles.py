# Day 11 - Plutonian Pebbles

import functools

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


@functools.lru_cache(maxsize=None)
def blink_single(stone):

    text = str(stone)

    if stone == 0:
        return (1, None)

    elif not len(text) % 2:

        first_stone = str(int(text[: int((len(text) / 2))]))
        second_stone = str(int(text[int(len(text) / 2) :]))
        return (int(first_stone), int(second_stone))

    else:
        return (stone * 2024, None)


@functools.lru_cache(maxsize=None)
def count_stones(stone, blinks):
    first_stone, second_stone = blink_single(stone)

    if blinks == 1:

        if second_stone is None:
            return 1
        else:
            return 2

    else:

        output = count_stones(first_stone, blinks - 1)
        if second_stone is not None:
            output += count_stones(second_stone, blinks - 1)

        return output


def num_of_stones_long(stones, count):
    stones = [int(stone) for stone in stones]

    output = 0

    for stone in stones:
        output += count_stones(stone, count)

    return output


assert num_of_stones_long(test_data, 25) == 55312

answer2 = num_of_stones_long(input, 75)
print(answer2)
