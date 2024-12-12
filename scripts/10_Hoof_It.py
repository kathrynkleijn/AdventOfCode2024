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
        self.debug = self.to_rows()
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

    # def make_move(self, current_row, current_col, previous_row, previous_col, height):
    #     if (
    #         current_col < self.n - 1
    #         and self.rows[current_row][current_col + 1] == height + 1
    #     ):
    #         previous_row, previous_col = current_row, current_col
    #         current_col += 1

    #     elif (
    #         current_row < self.m - 1
    #         and self.columns[current_col][current_row + 1] == height + 1
    #     ):
    #         previous_row, previous_col = current_row, current_col
    #         current_row += 1
    #     elif (
    #         current_row > 0 and self.columns[current_col][current_row - 1] == height + 1
    #     ):
    #         previous_row, previous_col = current_row, current_col
    #         current_row = current_row - 1
    #     elif current_col > 0 and self.rows[current_row][current_col - 1] == height + 1:
    #         previous_row, previous_col = current_row, current_col
    #         current_col = current_col - 1
    #     else:
    #         current_row, current_col = previous_row, previous_col
    #     return current_row, current_col, previous_row, previous_col

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
        alternatives = []
        height = 0
        trail = True
        while height < 9:
            if debug:
                # print(current_row, current_col, height)
                self.debug[current_row][current_col] = "X"
                debug_repr = ""
                for line in self.debug:
                    line = "".join(str(char) for char in line)
                    debug_repr += "\n" + line

                # print(debug_repr)
            moves = self.possible_moves(current_row, current_col, height)
            if not moves:
                current_row, current_col = previous_row, previous_col
                break
            elif len(moves) == 1:
                current_row, current_col, previous_row, previous_col = self.make_move(
                    current_row, current_col, previous_row, previous_col, moves[0]
                )
            else:
                alternatives = self.setup_alternatives(
                    current_row, current_col, moves[1:]
                )
                current_row, current_col, previous_row, previous_col = self.make_move(
                    current_row, current_col, previous_row, previous_col, moves[0]
                )

            height = self.rows[current_row][current_col]

        if debug:
            print(debug_repr)
            self.debug = self.to_rows()

        return trail, alternatives, current_row, current_col

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

    # def trail(self, trailhead, debug=False):
    #     current_row, current_col = trailhead
    #     previous_row, previous_col = trailhead
    #     height = 0
    #     trail = True
    #     while height < 9:
    #         if debug:
    #             print(current_row, current_col, height)
    #             self.debug[current_row][current_col] = "X"
    #             debug_repr = ""
    #             for line in self.debug:
    #                 line = "".join(str(char) for char in line)
    #                 debug_repr += "\n" + line

    #             print(debug_repr)
    #         current_row, current_col, previous_row, previous_col = self.make_move(
    #             current_row, current_col, previous_row, previous_col, height
    #         )
    #         if (previous_row, previous_col) == (current_row, current_col):
    #             trail = False
    #             break
    #         height = self.rows[current_row][current_col]

    #     return trail

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
        trailheads = [trailhead]
        tops = []
        while trailheads:
            trailhead = trailheads[0]
            top = self.check_top(trailhead)
            print(f"trailhead = {trailhead}")
            if top:
                trail = True
                current_row, current_col = trailhead
            else:
                trail, alternatives, current_row, current_col = self.trail(
                    trailhead, debug
                )
                trailheads.extend(alternatives)
            if trail:
                print(f"place = {current_row, current_col}")
                print(f"tops = {tops}")
                if (current_row, current_col) not in tops:
                    tops.append((current_row, current_col))
                    num_trails += 1
                else:
                    break
            if num_trails == len(self.ends):
                break
            print(f"tops = {tops}")
            print(f"num = {num_trails}")
            trailheads.pop(0)

        return num_trails

    def check_top(self, trailhead):
        row, col = trailhead
        if self.rows[row][col] == 9:
            return True
        else:
            return False


if __name__ == "__main__":

    test_map1 = HikingMap(test_data1)

    assert test_map1.possible_trailheads() == [(0, 0)]
    assert test_map1.possible_ends() == [(3, 0)]

    trailhead = test_map1.possible_trailheads()[0]

    # test_map1.trail(trailhead, debug=True)

    # print(test_map1.count_num_trails(trailhead))

    test_map2 = HikingMap(test_data2)

    assert len(test_map2.possible_trailheads()) == 9
    assert len(test_map2.possible_ends()) == 7

    # test_map2.trail((0, 2), debug=True)

    print(test_map2.count_num_trails((0, 2), debug=True))

    # works for some, but how do we go back and re-check the start?
