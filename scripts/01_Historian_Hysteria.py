# Day 1 - Historian Hysteria

test_data = """3   4
4   3
2   5
1   3
3   9
3   3"""
test_answer = 11


# Part 1


def extract_lists(data):
    lines = data.split("\n")
    lines = [line.split("   ") for line in lines]
    return [line[0] for line in lines], [line[1] for line in lines]


assert extract_lists(test_data) == (
    ["3", "4", "2", "1", "3", "3"],
    [
        "4",
        "3",
        "5",
        "3",
        "9",
        "3",
    ],
)


def sum_of_difference(list1, list2):
    sum = 0
    for i in range(len(list1)):
        sum += abs(int(list1[i]) - int(list2[i]))
    return sum


assert (
    sum_of_difference(
        ["1", "2", "3", "3", "3", "4"],
        [
            "3",
            "3",
            "3",
            "4",
            "5",
            "9",
        ],
    )
    == test_answer
)


with open("../input_data/01_Historian_Hysteria.txt", "r", encoding="utf-8") as file:
    input = file.read().strip()

in_list1, in_list2 = extract_lists(input)
answer_1 = sum_of_difference(sorted(in_list1), sorted(in_list2))
print(answer_1)


# Part 2

test_answer2 = 31


def similarity_score(list1, list2):
    sum = 0
    for i in range(len(list1)):
        count = list2.count(list1[i])
        sum += count * int(list1[i])
    return sum


assert (
    similarity_score(
        ["3", "4", "2", "1", "3", "3"],
        [
            "4",
            "3",
            "5",
            "3",
            "9",
            "3",
        ],
    )
    == test_answer2
)

answer_2 = similarity_score(in_list1, in_list2)
print(answer_2)
