# Day 5 - Print Queue
import math

# find number of numbers - if number in rule number-1 times then first?
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


def create_rule_list(rules):
    rule_list = rules[0].split("|")
    for rule in rules:
        first, second = rule.split("|")
        if first not in rule_list and second not in rule_list:
            rule_list.extend([first, second])
        elif first in rule_list and second not in rule_list:
            rule_list.append(second)
        elif first not in rule_list and second in rule_list:
            rule_list = rule_list[::-1]
            rule_list.append(first)
            rule_list = rule_list[::-1]
        else:
            first_index = rule_list.index(first)
            second_index = rule_list.index(second)
            if first_index > second_index:
                move = rule_list[second_index:first_index]
                rule_list = rule_list[:second_index] + rule_list[first_index:]
                rule_list.extend(move)
        # print(rule, rule_list)
    return rule_list


def create_rule_list_old(rules):
    rule_list = rules[0].split("|")
    for rule in rules:
        first, second = rule.split("|")
        if first not in rule_list and second not in rule_list:
            rule_list.extend([first, second])
        elif first in rule_list and second not in rule_list:
            rule_list.append(second)
        elif first not in rule_list and second in rule_list:
            rule_list = rule_list[::-1]
            rule_list.append(first)
            rule_list = rule_list[::-1]
        else:
            first_index = rule_list.index(first)
            second_index = rule_list.index(second)
            if first_index > second_index:
                rule_list.insert(second_index, rule_list.pop(first_index))
    return rule_list


def create_rule_list_old2(rules):
    rule_list = rules[0].split("|")
    for rule in rules:
        first, second = rule.split("|")
        if first not in rule_list and second not in rule_list:
            rule_list.insert(0, second)
            rule_list.insert(0, first)
        elif first in rule_list and second not in rule_list:
            rule_list.append(second)
        elif first not in rule_list and second in rule_list:
            rule_list.insert(0, first)
        else:
            first_index = rule_list.index(first)
            second_index = rule_list.index(second)
            if first_index > second_index:
                rule_list.insert(second_index, rule_list.pop(first_index))
    return rule_list


def create_rule_list_old3(rules):
    rule_list = rules[0].split("|")
    for rule in rules:
        first, second = rule.split("|")
        if first not in rule_list and second not in rule_list:
            rule_list.insert(0, first)
            rule_list.append(second)
        elif first in rule_list and second not in rule_list:
            rule_list.append(second)
        elif first not in rule_list and second in rule_list:
            rule_list.insert(0, first)
        else:
            first_index = rule_list.index(first)
            second_index = rule_list.index(second)
            if first_index > second_index:
                rule_list.insert(second_index, rule_list.pop(first_index))
    return rule_list


def create_rule_list_old4(rules):
    rule_list = rules[0].split("|")
    for rule in rules:
        first, second = rule.split("|")
        if first not in rule_list and second not in rule_list:
            rule_list.insert(0, first)
            rule_list.append(second)
        elif first in rule_list and second not in rule_list:
            first_index = rule_list.index(first)
            rule_list.insert(first_index + 1, second)
        elif first not in rule_list and second in rule_list:
            rule_list.insert(0, first)
        else:
            first_index = rule_list.index(first)
            second_index = rule_list.index(second)
            if first_index > second_index:
                rule_list.insert(second_index, rule_list.pop(first_index))
    return rule_list


# list of previous rules - move based on that?

assert create_rule_list([test_rules.split("\n")[0]]) == ["47", "53"]
test_rule_list = create_rule_list(test_rules.split("\n"))
test_rule_list_old = create_rule_list_old(test_rules.split("\n"))
test_rule_list_old2 = create_rule_list_old2(test_rules.split("\n"))
test_rule_list_old3 = create_rule_list_old3(test_rules.split("\n"))
test_rule_list_old4 = create_rule_list_old4(test_rules.split("\n"))
print(test_rule_list)
print(test_rule_list_old)
print(test_rule_list_old2)
print(test_rule_list_old3)
print(test_rule_list_old4)


def check_correct(rule_list, rules):
    for rule in rules:
        first, second = rule.split("|")
        first_index = rule_list.index(first)
        second_index = rule_list.index(second)
        if first_index > second_index:
            return False, rule
    return True, ""


# assert check_correct(test_rule_list, test_rules.split("\n"))[0] == True


def check_order(line, rule_list):
    line = line.split(",")
    check_list = [num for num in rule_list if num in line]
    return line == check_list


# assert check_order("75,47,61,53,29", test_rule_list) == True


def sum_of_middle(rule_list, lines):
    sum = 0
    for line in lines:
        if check_order(line, rule_list):
            sum += int(line.split(",")[math.floor(len(line.split(",")) / 2)])
    return sum


# assert sum_of_middle(test_rule_list, test_lines.split("\n")) == test_answer


with open("../input_data/05_Print_Queue.txt", "r", encoding="utf-8") as file:
    input_rules, input_lines = file.read().strip().split("\n\n")


test_list_2 = input_rules.split("\n")[:29]
rule_list = create_rule_list(test_list_2)
rule_list_old = create_rule_list_old(test_list_2)
rule_list_old2 = create_rule_list_old2(test_list_2)
rule_list_old3 = create_rule_list_old3(test_list_2)
rule_list_old4 = create_rule_list_old4(test_list_2)
print(rule_list)
print(rule_list_old)
print(rule_list_old2)
print(rule_list_old3)
print(rule_list_old4)
print(check_correct(rule_list, test_list_2))  # 85|43, [:27]
print(check_correct(rule_list_old, test_list_2))  # 91|77 [:29]
print(check_correct(rule_list_old2, test_list_2))  # 91|77 [:29]
print(check_correct(rule_list_old3, test_list_2))  # 91|77 [:29]
print(check_correct(rule_list_old4, test_list_2))  # 91|77 [:29]
# input_rule_list = create_rule_list(input_rules.split("\n"))
# print(input_rule_list)

# print(check_correct(input_rule_list, input_rules.split("\n")))
# answer1 = sum_of_middle(input_rule_list, input_lines.split("\n"))
# print(answer1)
