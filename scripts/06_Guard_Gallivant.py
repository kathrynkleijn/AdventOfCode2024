# Day 6 - Guard Gallivant

import math

test_data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

test_answer = 41


class LabMap:
    def __init__(self, map):
        self.map = map
        self.lines = map.split("\n")
        self.m = len(self.lines[0])
        self.n = len(self.lines)
        self.size = (self.m, self.n)
        self.start = self.start_point()

    def __str__(self):
        return "\n".join(line for line in self.lines)

    def start_point(self):
        row_num = math.floor(self.map.find("^") / (self.m + 3)) + 1
        column_num = self.lines[row_num].find("^")
        return (row_num, column_num)

    def make_step(self, start, direction):
        current_row, current_col = start
        self.lines[current_row] = (
            self.lines[current_row][:current_col]
            + "X"
            + self.lines[current_row][current_col + 1 :]
        )
        if direction == "^":
            if current_row == 0:
                pass
            elif self.lines[current_row - 1][current_col] == "#":
                direction = ">"
                current_col += 1
            else:
                current_row = current_row - 1
        elif direction == ">":
            if current_col == self.n - 1:
                pass
            elif self.lines[current_row][current_col + 1] == "#":
                direction = "v"
                current_row += 1
            else:
                current_col += 1
        elif direction == "v":
            if current_row == self.m - 1:
                pass
            elif self.lines[current_row + 1][current_col] == "#":
                direction = "<"
                current_col = current_col - 1
            else:
                current_row += 1
        else:
            if current_col == 0:
                pass
            elif self.lines[current_row][current_col - 1] == "#":
                direction = "^"
                current_row = current_row - 1
            else:
                current_col = current_col - 1
        return current_row, current_col, direction

    def walk(self, debug=False):
        current_row, current_col = self.start
        direction = self.lines[current_row][current_col]
        position_count = 0
        while current_row in range(self.m - 1) and current_col in range(self.n - 1):
            current_row, current_col, direction = self.make_step(
                (current_row, current_col), direction
            )
            if self.lines[current_row][current_col] != "X":
                position_count += 1
            if debug == True:
                print("\n")
                print(self)
        current_row, current_col, direction = self.make_step(
            (current_row, current_col), direction
        )
        position_count += 1
        if debug == True:
            print("\n")
            print(self)
        return position_count


if __name__ == "__main__":

    test_map = LabMap(test_data)
    assert test_map.walk() == test_answer

    with open("../input_data/06_Guard_Gallivant.txt", "r", encoding="utf-8") as file:
        input = file.read()

    answer_map = LabMap(input)
    print(answer_map.start)
    answer1 = answer_map.walk()
    print(answer1)
