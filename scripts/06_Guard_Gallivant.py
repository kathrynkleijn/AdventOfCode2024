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
test_answer2 = 6


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

    def make_step(self, start, direction, obstructed=False):
        current_row, current_col = start
        if obstructed:
            if self.lines[current_row][current_col] == "X":
                self.lines[current_row] = (
                    self.lines[current_row][:current_col]
                    + "1"
                    + self.lines[current_row][current_col + 1 :]
                )
            else:
                visits = int(self.lines[current_row][current_col]) + 1
                self.lines[current_row] = (
                    self.lines[current_row][:current_col]
                    + f"{visits}"
                    + self.lines[current_row][current_col + 1 :]
                )
            if self.lines[current_row][current_col].isdigit():
                if int(self.lines[current_row][current_col]) > 3:
                    return 0, 0, False
        else:
            self.lines[current_row] = (
                self.lines[current_row][:current_col]
                + "X"
                + self.lines[current_row][current_col + 1 :]
            )
        if direction == "^":
            if current_row == 0:
                pass
            elif (
                self.lines[current_row - 1][current_col] == "#"
                or self.lines[current_row - 1][current_col] == "O"
            ):
                direction = ">"
                current_col += 1
            else:
                current_row = current_row - 1
        elif direction == ">":
            if current_col == self.n - 1:
                pass
            elif (
                self.lines[current_row][current_col + 1] == "#"
                or self.lines[current_row][current_col + 1] == "O"
            ):
                direction = "v"
                current_row += 1
            else:
                current_col += 1
        elif direction == "v":
            if current_row == self.m - 1:
                pass
            elif (
                self.lines[current_row + 1][current_col] == "#"
                or self.lines[current_row + 1][current_col] == "O"
            ):
                direction = "<"
                current_col = current_col - 1
            else:
                current_row += 1
        else:
            if current_col == 0:
                pass
            elif (
                self.lines[current_row][current_col - 1] == "#"
                or self.lines[current_row][current_col - 1] == "O"
            ):
                direction = "^"
                current_row = current_row - 1
            else:
                current_col = current_col - 1
        return current_row, current_col, direction

    def walk(self, obstructed=False, debug=False):
        current_row, current_col = self.start
        direction = self.lines[current_row][current_col]
        position_count = 0
        while current_row in range(self.m - 1) and current_col in range(self.n - 1):
            current_row, current_col, direction = self.make_step(
                (current_row, current_col), direction, obstructed
            )
            if not direction:
                break
            else:
                if self.lines[current_row][current_col] != "X":
                    position_count += 1
            if debug == True:
                print("\n")
                print(self)
        if not obstructed:
            current_row, current_col, direction = self.make_step(
                (current_row, current_col), direction
            )
            position_count += 1
            if debug == True:
                print("\n")
                print(self)
        return position_count

    def add_obstruction(self, position):
        row, col = position
        self.lines[row] = self.lines[row][:col] + "O" + self.lines[row][col + 1 :]

    def remove_obstruction(self):
        row = math.floor(self.map.find("O") / (self.m + 3)) + 1
        col = self.lines[row].find("O")
        self.lines[row] = self.lines[row][:col] + "." + self.lines[row][col + 1 :]

    def non_obstructed_spaces(self):
        positions = []
        for row, line in enumerate(self.lines):
            for col, char in enumerate(line):
                if char == "X" and (row, col) != self.start:
                    positions.append((row, col))
        return positions

    def test_for_loops(self, positions, debug=False):
        loops_found = 0
        for position in positions:
            print(position)
            self.add_obstruction(position)
            loop = self.walk(obstructed=True, debug=debug)
            if loop:
                print("loop")
                loops_found += 1
                print(loops_found)
            self.remove_obstruction()
        return loops_found

    def reset_lines(self):
        self.lines = self.map.split("\n")


if __name__ == "__main__":

    test_map = LabMap(test_data)
    assert test_map.walk() == test_answer

    # with open("../input_data/06_Guard_Gallivant.txt", "r", encoding="utf-8") as file:
    #     input = file.read()

    # answer_map = LabMap(input)
    # print(answer_map.start)
    # answer1 = answer_map.walk()
    # print(answer1)

    # positions = test_map.non_obstructed_spaces()

    positions = [(6, 3), (7, 6)]  # , (7, 7), (8, 1), (8, 3), (9, 7)]
    print(test_map.test_for_loops(positions))

    # test_map.reset_lines()
    # test_map.walk()
    # print(test_map.test_for_loops([(1, 4)]))

    # keep an eye on all places visitied - if ==2 then it's a loop
