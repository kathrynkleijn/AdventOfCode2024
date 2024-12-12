# Day 10 - Hoof It

from collections import defaultdict, OrderedDict

test_data1 = """0123
1234
8765
9876"""

test_data2 = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

test_answer1 = 1
test_answer2 = 36

test_data3 = """...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9"""

test_data4 = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""

test_data5 = """10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01"""


class HikingMap:

    def __init__(self, map):
        self.map = map
        self.rows = self.to_rows()
        self.columns = self.to_columns()
        self.m = len(self.rows)
        self.n = len(self.columns)
        self.size = (self.m, self.n)
        self.debug = self.to_rows()
        self.ends = self.possible_ends()

    def __str__(self):
        return "\n".join(line for line in self.rows)

    def to_rows(self):
        rows = []
        lines = self.map.split("\n")
        for line in lines:
            row = [char for char in line]
            for i in range(len(row)):
                if row[i] != ".":
                    row[i] = int(row[i])

            rows.append(row)
        return rows

    def to_columns(self):
        columns = []
        for col in range(len(self.rows[0])):
            columns.append([row[col] for row in self.rows])
        return columns

    def make_move(self, current_row, current_col, previous_row, previous_col, move):
        if move == "right":
            previous_row, previous_col = current_row, current_col
            current_col += 1

        elif move == "down":
            previous_row, previous_col = current_row, current_col
            current_row += 1
        elif move == "up":
            previous_row, previous_col = current_row, current_col
            current_row = current_row - 1
        elif move == "left":
            current_col = current_col - 1
        return current_row, current_col, previous_row, previous_col

    def possible_moves(self, current_row, current_col, height):
        moves = []

        if (
            current_col < self.n - 1
            and self.rows[current_row][current_col + 1] != "."
            and self.rows[current_row][current_col + 1] == height + 1
        ):
            moves.append("right")
        if (
            current_row < self.m - 1
            and self.columns[current_col][current_row + 1] != "."
            and self.columns[current_col][current_row + 1] == height + 1
        ):
            moves.append("down")
        if (
            current_row > 0
            and self.columns[current_col][current_row - 1] != "."
            and self.columns[current_col][current_row - 1] == height + 1
        ):
            moves.append("up")
        if (
            current_col > 0
            and self.rows[current_row][current_col - 1]
            and self.rows[current_row][current_col - 1] == height + 1
        ):
            moves.append("left")
        return moves

    def trail(self, trailhead, height, debug=False):
        current_row, current_col = trailhead
        previous_row, previous_col = trailhead
        alternatives = defaultdict()
        height = height
        trail = True
        while height < 9:
            if debug:
                print(current_row, current_col, height)
                self.debug[current_row][current_col] = "X"
                debug_repr = ""
                for line in self.debug:
                    line = "".join(str(char) for char in line)
                    debug_repr += "\n" + line

                print(debug_repr)
            moves = self.possible_moves(current_row, current_col, height)
            if not moves:
                current_row, current_col = previous_row, previous_col
                trail = False
                break
            elif len(moves) == 1:
                current_row, current_col, previous_row, previous_col = self.make_move(
                    current_row, current_col, previous_row, previous_col, moves[0]
                )
            else:
                alts = self.setup_alternatives(current_row, current_col, moves[1:])
                current_row, current_col, previous_row, previous_col = self.make_move(
                    current_row, current_col, previous_row, previous_col, moves[0]
                )
                for alt in alts:
                    alternatives[alt] = height + 1

            height = self.rows[current_row][current_col]

        if debug:
            print(debug_repr)
            self.debug = self.to_rows()

        return trail, alternatives, current_row, current_col, height

    def setup_alternatives(self, current_row, current_col, moves):
        alternatives = []
        for move in moves:
            new_row, new_col = current_row, current_col
            if move == "right":
                new_col = current_col + 1
            elif move == "down":
                new_row = current_row + 1
            elif move == "left":
                new_col = current_col - 1
            elif move == "up":
                new_row = current_row - 1
            alternatives.append((new_row, new_col))
        return alternatives

    def possible_trailheads(self):
        trailheads = []
        for num, row in enumerate(self.rows):
            try:
                cols = [col for col, item in enumerate(row) if item == 0]
                for col in cols:
                    trailheads.append((num, col))
            except:
                continue
        return trailheads

    def possible_ends(self):
        ends = []
        for num, row in enumerate(self.rows):
            try:
                cols = [col for col, item in enumerate(row) if item == 9]
                for col in cols:
                    ends.append((num, col))
            except:
                continue
        return ends

    def count_num_trails(self, trailhead, debug=False):
        rating = 0
        num_trails = 0
        trailheads = OrderedDict()
        trailheads[trailhead] = 0
        checked = []
        tops = []
        while trailheads:
            trailhead = list(trailheads.keys())[0]
            height = trailheads[trailhead]
            if trailhead in checked:
                trailheads.pop(trailhead, None)
                rating += 1
                continue
            top = self.check_top(trailhead)
            if top:
                trail = True
                current_row, current_col = trailhead
            else:
                trail, alternatives, current_row, current_col, height = self.trail(
                    trailhead, height, debug
                )
                for alternative, height in alternatives.items():
                    trailheads[alternative] = height
            if trail:
                if (current_row, current_col) not in tops:
                    tops.append((current_row, current_col))
                    num_trails += 1
                rating += 1
            if num_trails == len(self.ends):
                break
            try:
                trailheads.pop(trailhead)
            except:
                break

            checked.append(trailhead)
            checked = list(set(checked))
        return num_trails, rating

    def check_top(self, trailhead):
        row, col = trailhead
        if self.rows[row][col] == 9:
            return True
        else:
            return False

    def count_all_trails(self, debug=False):
        total = 0
        rating = 0
        trailheads = self.possible_trailheads()
        for trailhead in trailheads:
            tot, rate = self.count_num_trails(trailhead, debug)
            total += tot
            rating += rate
        return total, rating


if __name__ == "__main__":

    test_map1 = HikingMap(test_data1)

    assert test_map1.possible_trailheads() == [(0, 0)]
    assert test_map1.possible_ends() == [(3, 0)]

    trailhead = test_map1.possible_trailheads()[0]

    # test_map1.trail(trailhead, debug=True)

    assert test_map1.count_num_trails(trailhead)[0] == 1
    assert test_map1.count_all_trails()[0] == test_answer1

    test_map2 = HikingMap(test_data2)

    assert len(test_map2.possible_trailheads()) == 9
    assert len(test_map2.possible_ends()) == 7

    # test_map2.trail((0, 2), debug=True)

    assert test_map2.count_all_trails()[0] == test_answer2

    test_map3 = HikingMap(test_data3)
    assert test_map3.count_all_trails()[0] == 2
    test_map4 = HikingMap(test_data4)
    assert test_map4.count_all_trails()[0] == 4
    test_map5 = HikingMap(test_data5)
    assert test_map5.count_all_trails()[0] == 3

    with open("../input_data/10_Hoof_It.txt", "r", encoding="utf-8") as file:
        input = file.read().strip()

    answer_map = HikingMap(input)
    answer1 = answer_map.count_all_trails()[0]
    print(answer1)

    # Part 2

    print(test_map2.count_all_trails())
    assert test_map2.count_all_trails()[1] == 81
