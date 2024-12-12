# Day 10 - Hoof It

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
test_answer2 = 9


class HikingMap:

    def __init__(self, map):
        self.map = map
        self.rows = self.to_rows()
        self.columns = self.to_columns()
        self.m = len(self.rows)
        self.n = len(self.columns)
        self.size = (self.m, self.n)
        self.debug = self.rows.copy()
        self.ends = self.possible_ends()

    def __str__(self):
        return "\n".join(line for line in self.rows)

    def to_rows(self):
        self.rows = []
        lines = self.map.split("\n")
        for line in lines:
            self.rows.append([int(char) for char in line])
        return self.rows

    def to_columns(self):
        self.columns = []
        for col in range(len(self.rows[0])):
            self.columns.append([row[col] for row in self.rows])
        return self.columns

    def make_move(self, current_row, current_col, previous_row, previous_col, height):
        if (
            current_col < self.n - 1
            and self.rows[current_row][current_col + 1] == height + 1
        ):
            previous_row, previous_col = current_row, current_col
            current_col += 1

        elif (
            current_row < self.m - 1
            and self.columns[current_col][current_row + 1] == height + 1
        ):
            previous_row, previous_col = current_row, current_col
            current_row += 1
        elif (
            current_row > 0 and self.columns[current_col][current_row - 1] == height + 1
        ):
            previous_row, previous_col = current_row, current_col
            current_row = current_row - 1
        elif current_col > 0 and self.rows[current_row][current_col - 1] == height + 1:
            previous_row, previous_col = current_row, current_col
            current_col = current_col - 1
        else:
            current_row, current_col = previous_row, previous_col
        return current_row, current_col, previous_row, previous_col

    def possible_moves(self, current_row, current_col, height):
        moves = []
        if (
            current_col < self.n - 1
            and self.rows[current_row][current_col + 1] == height + 1
        ):
            moves.append("right")

        if (
            current_row < self.m - 1
            and self.columns[current_col][current_row + 1] == height + 1
        ):
            moves.append("down")
        if current_row > 0 and self.columns[current_col][current_row - 1] == height + 1:
            moves.append("up")
        if current_col > 0 and self.rows[current_row][current_col - 1] == height + 1:
            moves.append("left")
        return moves

    def trail(self, trailhead, debug=False):
        current_row, current_col = trailhead
        previous_row, previous_col = trailhead
        height = 0
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
            current_row, current_col, previous_row, previous_col = self.make_move(
                current_row, current_col, previous_row, previous_col, height
            )
            if (previous_row, previous_col) == (current_row, current_col):
                trail = False
                break
            height = self.rows[current_row][current_col]

        return trail

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
        num_trails = 0
        # loop over possibilities
        while ...:
            if num_trails == len(self.ends):
                break

        return num_trails


if __name__ == "__main__":

    test_map1 = HikingMap(test_data1)

    assert test_map1.possible_trailheads() == [(0, 0)]
    assert test_map1.possible_ends() == [(3, 0)]

    trailhead = test_map1.possible_trailheads()[0]

    # test_map1.trail(trailhead, debug=True)

    test_map2 = HikingMap(test_data2)

    assert len(test_map2.possible_trailheads()) == 9
    assert len(test_map2.possible_ends()) == 7

    # test_map2.trail((0, 2), debug=True)
