# Day 11 - Plutonian Pebbles

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

answer2 = num_of_stones(input, 75)
print(answer2)
