# Day 5 - Print Queue
import math
import collections


test_data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

test_rules, test_lines = test_data.split("\n\n")
test_answer = 143
test_answer2 = 123


def check_order(line, rules):
    if type(line) == str:
        line = line.split(",")
    for rule in rules:
        first, second = rule.split("|")
        if first in line and second in line:
            first_index = line.index(first)
            second_index = line.index(second)
            if first_index > second_index:
                return False
    return True


assert check_order("75,47,61,53,29", test_rules.split("\n")) == True


def sum_of_middle(rules, lines):
    sum = 0
    for line in lines:
        if check_order(line, rules):
            sum += int(line.split(",")[math.floor(len(line.split(",")) / 2)])
    return sum


assert sum_of_middle(test_rules.split("\n"), test_lines.split("\n")) == test_answer


with open("../input_data/05_Print_Queue.txt", "r", encoding="utf-8") as file:
    input_rules, input_lines = file.read().strip().split("\n\n")


answer1 = sum_of_middle(input_rules.split("\n"), input_lines.split("\n"))
print(answer1)


# Part 2


def corrected_line(rules, line):
    if type(line) == str:
        line = line.split(",")
    for rule in rules:
        first, second = rule.split("|")
        if first in line and second in line:
            first_index = line.index(first)
            second_index = line.index(second)
            if first_index > second_index:
                line.insert(second_index, line.pop(first_index))
    return line


def sum_of_middle_incorrect(rules, lines):
    sum = 0
    for line in lines:
        if not check_order(line, rules):
            while not check_order(line, rules):
                line = corrected_line(rules, line)

            sum += int(line[math.floor(len(line) / 2)])
    return sum


assert (
    sum_of_middle_incorrect(test_rules.split("\n"), test_lines.split("\n"))
    == test_answer2
)

answer2 = sum_of_middle_incorrect(input_rules.split("\n"), input_lines.split("\n"))
print(answer2)
