# Day 2 - Red-Nosed Reports

import collections

test_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".strip().split(
    "\n"
)

test_answer = 2


def check_safe(report):
    if len(set(report)) != len(report):
        return 0
    elif (sorted(report) != report) and (sorted(report, reverse=True) != report):
        return 0
    else:
        for i in range(len(report) - 1):
            if abs(int(report[i + 1]) - int(report[i])) > 3:
                return 0
        return 1


assert check_safe([8, 7, 4, 4, 1]) == 0
assert check_safe([7, 6, 4, 2, 1]) == 1
assert check_safe([1, 2, 7, 8, 9]) == 0
assert check_safe([9, 7, 6, 2, 1]) == 0

assert check_safe([4, 7, 8, 9, 12, 14, 15, 18]) == 1


def total_safe_reports(report_list):
    safe_total = 0
    for report in report_list:
        report = list(map(int, report.split()))
        safe_total += check_safe(report)
    return safe_total


assert total_safe_reports(test_data) == test_answer


with open("../input_data/02_Red-Nosed_Reports.txt", "r", encoding="utf-8") as file:
    input = file.read().strip().split("\n")

answer_1 = total_safe_reports(input)
print(answer_1)

# Part 2

test_answer2 = 4


def duplicates_check(report):
    dups = collections.defaultdict(list)
    for i, e in enumerate(report):
        dups[e].append(i)
    for v in dups.values():
        if len(v) >= 2:
            return v


def check_safe_with_dampener(report):
    if len(set(report)) != len(report):
        if len(set(report)) == len(report) - 1:
            duplicate_indices = duplicates_check(report)
            if duplicate_indices[1] - duplicate_indices[0] == 1:
                report.pop(duplicate_indices[0])
                return check_safe(report)
            else:
                rep1 = report.copy()
                rep1.pop(duplicate_indices[0])
                drop_first = check_safe(rep1)
                rep2 = report.copy()
                rep2.pop(duplicate_indices[1])
                drop_second = check_safe(rep2)
                if drop_first == 1 or drop_second == 1:
                    return 1
                else:
                    return 0
        else:
            return 0
    elif (sorted(report) != report) and (sorted(report, reverse=True) != report):
        report_copy = report.copy()
        report_copy.pop(0)
        if check_safe(report_copy) == 1:
            return 1
        elif report[1] - report[0] > 0:
            for i in range(1, len(report) - 1):
                if report[i + 1] - report[i] < 0:
                    report_copy = report.copy()
                    report_copy.pop(i)
                    check1 = check_safe(report_copy)
                    report.pop((i + 1))
                    check2 = check_safe(report)
                    if check1 == 1 or check2 == 1:
                        return 1
                    else:
                        return 0

        else:
            for i in range(1, len(report) - 1):
                if report[i + 1] - report[i] > 0:
                    report_copy = report.copy()
                    report_copy.pop(i)
                    check1 = check_safe(report_copy)
                    report.pop((i + 1))
                    check2 = check_safe(report)
                    if check1 == 1 or check2 == 1:
                        return 1
                    else:
                        return 0
    else:
        if abs(int(report[1]) - int(report[0])) > 3:
            report = report[1:]
            return check_safe(report)
        elif abs(int(report[-1]) - int(report[-2])) > 3:
            report = report[:-1]
            return check_safe(report)
        else:
            for i in range(len(report) - 1):
                if abs(int(report[i + 1]) - int(report[i])) > 3:
                    return 0
        return 1


assert check_safe_with_dampener([5, 5, 8, 5, 2]) == 0
assert check_safe_with_dampener([51, 52, 55, 58, 60, 61, 62, 61]) == 1
assert check_safe_with_dampener([71, 68, 71, 78, 79, 78]) == 0
assert check_safe_with_dampener([1, 1, 2, 8, 9, 12, 10]) == 0
assert check_safe_with_dampener([1, 6, 3, 4, 7]) == 1
assert check_safe_with_dampener([1, 7, 8, 9, 10]) == 1
assert check_safe_with_dampener([7, 8, 9, 10, 15]) == 1
assert check_safe_with_dampener([10, 9, 8, 7, 1]) == 1
assert check_safe_with_dampener([15, 10, 9, 8, 7]) == 1
assert check_safe_with_dampener([20, 23, 22, 19, 17, 15]) == 1
assert check_safe_with_dampener([21, 22, 25, 28, 31, 29, 34]) == 1


def apply_problem_dampener(report_list):
    safe_total = 0
    for report in report_list:
        report = list(map(int, report.split()))
        safe_total += check_safe_with_dampener(report)
    return safe_total


assert apply_problem_dampener(test_data) == test_answer2


answer_2 = apply_problem_dampener(input)
print(answer_2)


# brute force
def brute_force(report_list):
    safe_total = 0
    for report in report_list:
        report = list(map(int, report.split()))
        rep_check = 0
        for i in range(len(report)):
            new = report.copy()
            new.pop(i)
            rep_check += check_safe(new)
        if rep_check > 0:
            safe_total += 1
    return safe_total


answer = brute_force(input)
print(answer)
