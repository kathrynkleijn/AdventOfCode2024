# Day 2 - Red-Nosed Reports

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


def check_safe_with_dampener(report):
    if len(set(report)) != len(report):
        return 0.1
    elif (sorted(report) != report) and (sorted(report, reverse=True) != report):
        return 0.2
    else:
        for i in range(len(report) - 1):
            if abs(int(report[i + 1]) - int(report[i])) > 3:
                return 0.3
        return 1


def apply_problem_dampener(report_list):
    safe_total = 0
    for report in report_list:
        report = list(map(int, report.split()))
        category = check_safe_with_dampener(report)
        if category == 1:
            safe_total += 1
        else:
            safe_total += problem_dampener(report, category)
    return safe_total


def problem_dampener(report, category):
    if category == 0.1:
        for i in range(len(report) - 1):
            if report[i + 1] == report[i]:
                report.remove(report[i])
                return check_safe(report)
    elif category == 0.2:
        if report[1] - report[0] > 0:
            for i in range(1, len(report) - 1):
                if report[i + 1] - report[i] < 0:
                    report.remove(report[i])
                    return check_safe(report)
        else:
            for i in range(1, len(report) - 1):
                if report[i + 1] - report[i] > 0:
                    report = report.remove(report[i])
                    return check_safe(report)
    else:
        return 0


assert apply_problem_dampener(test_data) == test_answer2
