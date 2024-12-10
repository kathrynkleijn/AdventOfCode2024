# Day 6 - Guard Gallivant

import math
import collections

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
        # self.debug_map = map.split("\n")
        self.columns = self.to_columns()
        self.m = len(self.lines)
        self.n = len(self.columns)
        self.size = (self.m, self.n)
        self.start = self.start_point()
        self.visited = collections.defaultdict(list)
        self.start_direction = self.lines[self.start[0]][self.start[1]]

    def __str__(self):
        return "\n".join(line for line in self.lines)

    def start_point(self):
        row_num = math.floor(self.map.find("^") / (self.m + 3)) + 1
        column_num = self.lines[row_num].find("^")
        return (row_num, column_num)

    def to_columns(self):
        self.columns = []
        for col in range(len(self.lines[0])):
            self.columns.append("".join(row[col] for row in self.lines))
        return self.columns

    def find_next_obstruction(self, current_row, current_col, direction):
        new_position = (current_row, current_col)
        if direction == "^":
            try:
                next_obstruction = self.columns[current_col][:current_row][::-1].find(
                    "#"
                )
                next_obstruction = (
                    len(self.columns[current_col][:current_row]) - next_obstruction
                ) - 1
            except:
                next_obstruction = -1
            if next_obstruction < new_position[0] - 1 and next_obstruction >= 0:
                new_position = (next_obstruction + 1, current_col)
                for row in range(new_position[0], current_row + 1):
                    self.lines[row] = (
                        self.lines[row][:current_col]
                        + "X"
                        + self.lines[row][current_col + 1 :]
                    )
            else:
                new_position = (-1, -1)
                for row in range(current_row + 1):
                    self.lines[row] = (
                        self.lines[row][:current_col]
                        + "X"
                        + self.lines[row][current_col + 1 :]
                    )
            direction = ">"

        elif direction == ">":
            try:
                next_obstruction = (
                    self.lines[current_row][current_col:].find("#") + current_col
                )
            except:
                next_obstruction = -1
            if next_obstruction > new_position[1] + 1:
                new_position = (current_row, next_obstruction - 1)
                num_moves = new_position[1] - current_col + 1
                self.lines[current_row] = (
                    self.lines[current_row][:current_col]
                    + "X" * num_moves
                    + self.lines[current_row][new_position[1] + 1 :]
                )
            else:
                new_position = (-1, -1)
                self.lines[current_row] = self.lines[current_row][
                    :current_col
                ] + "X" * (self.n - current_col)
            direction = "v"
        elif direction == "v":
            try:
                next_obstruction = (
                    self.columns[current_col][current_row:].find("#") + current_row
                )
            except:
                next_obstruction = -1
            if next_obstruction > new_position[0] + 1:
                new_position = (next_obstruction - 1, current_col)
                for row in range(current_row, new_position[0] + 1):
                    self.lines[row] = (
                        self.lines[row][:current_col]
                        + "X"
                        + self.lines[row][current_col + 1 :]
                    )
            else:
                new_position = (-1, -1)
                for row in range(current_row, self.n):
                    self.lines[row] = (
                        self.lines[row][:current_col]
                        + "X"
                        + self.lines[row][current_col + 1 :]
                    )
            direction = "<"
        else:
            try:
                next_obstruction = self.lines[current_row][:current_col][::-1].find("#")
                next_obstruction = (
                    len(self.lines[current_row][:current_col]) - next_obstruction
                ) - 1
            except:
                next_obstruction = -1
            if next_obstruction < new_position[1] - 1 and next_obstruction >= 0:
                new_position = (current_row, next_obstruction + 1)
                num_moves = current_col - new_position[1] + 1
                self.lines[current_row] = (
                    self.lines[current_row][: new_position[1]]
                    + "X" * num_moves
                    + self.lines[current_row][current_col + 1 :]
                )
            else:
                new_position = (-1, -1)
                self.lines[current_row] = (
                    "X" * current_col + self.lines[current_row][current_col + 1 :]
                )

            direction = "^"
        return new_position, direction

    def make_move(self, start, direction, obstructed=False, debug=False):
        current_row, current_col = start
        (current_row, current_col), direction = self.find_next_obstruction(
            current_row, current_col, direction
        )
        if obstructed:
            self.visited[(current_row, current_col)].append(direction)

        return current_row, current_col, direction

    def walk(self, obstructed=False, debug=False):
        current_row, current_col = self.start
        direction = self.start_direction
        outside = False
        position_count = True
        while current_row in range(self.m - 1) and current_col in range(self.n - 1):
            current_row, current_col, direction = self.make_move(
                (current_row, current_col), direction, obstructed, debug
            )
            if debug == True:
                print("\n")
                print(self)
                print(current_row, current_col)

            if current_row < 0 or current_col < 0:
                outside = True
                break

            if obstructed:
                count = collections.Counter(self.visited[(current_row, current_col)])
                if count[direction] > 1:
                    position_count = False
                    break
                else:
                    continue
        if position_count:
            position_count = 0
            for line in self.lines:
                position_count += collections.Counter(line)["X"]
            if not outside:
                position_count += 1
        return position_count

    def add_obstruction(self, position):
        row, col = position
        self.lines[row] = self.lines[row][:col] + "#" + self.lines[row][col + 1 :]
        self.columns[col] = self.columns[col][:row] + "#" + self.columns[col][row + 1 :]

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
            self.add_obstruction(position)
            count = self.walk(obstructed=True, debug=debug)
            if not count:
                loops_found += 1
            self.reset()
        return loops_found

    def reset(self):
        self.lines = self.map.split("\n")
        self.visited = collections.defaultdict(list)


if __name__ == "__main__":

    test_map = LabMap(test_data)
    assert test_map.walk() == test_answer

    with open("../input_data/06_Guard_Gallivant.txt", "r", encoding="utf-8") as file:
        input = file.read().strip()

    answer_map = LabMap(input)

    print(answer_map.start)
    answer1 = answer_map.walk()
    print(answer1)

    test_map.reset()
    positions = [(6, 3), (7, 6), (7, 7), (8, 1), (8, 3), (9, 7)]
    assert test_map.test_for_loops(positions) == 6

    test_map.reset()
    test_map.walk()
    positions = test_map.non_obstructed_spaces()
    test_map.reset()
    assert test_map.test_for_loops(positions) == test_answer2

    # answer_positions = answer_map.non_obstructed_spaces()
    # answer2 = answer_map.test_for_loops(answer_positions)
    # print(answer2)

# 1794 too low (and slow)
