# Day 4 - Ceres Search

import regex as re

test_data1 = """..X...
.SAMX.
.A..A.
XMAS.S
.X...."""

test_data2 = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

test_data3 = """....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX"""

test_answer = 18

test_data4 = """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
.........."""

test_answer2 = 9


class WordSearch:

    def __init__(self, grid):
        self.grid = grid
        self.rows = grid.split("\n")
        self.columns = self.to_columns()
        self.m = len(self.rows)
        self.n = len(self.columns)
        self.size = (self.m, self.n)
        self.diagonalsLR = self.to_diagonalsLR()
        self.diagonalsRL = self.to_diagonalsRL()

    def to_columns(self):
        self.columns = []
        for col in range(len(self.rows[0])):
            self.columns.append("".join(row[col] for row in self.rows))
        return self.columns

    def to_diagonalsLR(self):
        self.diagonals = []
        row = 0
        if self.m == self.n:
            for j in range(self.n):
                diagonal = ""
                for i in range(row, self.m - j):
                    diagonal += self.rows[i][i + j]
                self.diagonals.append(diagonal)
            for row in range(1, self.n):
                diagonal = ""
                for j in range(self.m - row):
                    diagonal += self.rows[row + j][j]
                self.diagonals.append(diagonal)

        else:
            j = 0
            diagonal = ""
            for i in range(row, self.m - j):
                diagonal += self.rows[i][i + j]
            self.diagonals.append(diagonal)
            for j in range(1, self.n):
                diagonal = ""
                for i in range(row, self.m - j + 1):
                    diagonal += self.rows[i][i + j]
                self.diagonals.append(diagonal)
            for row in range(1, self.n - 1):
                diagonal = ""
                for j in range(self.m - row):
                    diagonal += self.rows[row + j][j]
                self.diagonals.append(diagonal)

        return self.diagonals

    def to_diagonalsRL(self):
        self.diagonals = []
        row = self.m - 1
        if self.m == self.n:
            for j in range(self.n):
                diagonal = ""
                for i in range(self.m - j):
                    if row - i < 0:
                        continue
                    diagonal += self.rows[row - i][i + j]
                self.diagonals.append(diagonal)
            for row in reversed(range(self.n - 1)):
                diagonal = ""
                for j in range(row + 1):
                    diagonal += self.rows[row - j][j]
                self.diagonals.append(diagonal)

        else:
            for j in range(self.n):
                diagonal = ""
                for i in range(self.m - j + 1):
                    if row - i < 0:
                        continue
                    diagonal += self.rows[row - i][i + j]
                self.diagonals.append(diagonal)
            for row in reversed(range(self.n - 2)):
                diagonal = ""
                for j in range(row + 1):
                    diagonal += self.rows[row - j][j]
                self.diagonals.append(diagonal)

        return self.diagonals

    def find_word(self, word, debug=False):
        if debug == True:
            rows = " ".join(place for place in self.rows)
            number_r = len(re.findall(f"({word}|{word[::-1]})", rows, overlapped=True))
            columns = " ".join(place for place in self.columns)
            number_c = len(
                re.findall(f"({word}|{word[::-1]})", columns, overlapped=True)
            )
            diagonal1 = " ".join(place for place in self.diagonalsLR)
            number_d1 = len(
                re.findall(f"({word}|{word[::-1]})", diagonal1, overlapped=True)
            )
            diagonal2 = " ".join(place for place in self.diagonalsRL)
            number_d2 = len(
                re.findall(f"({word}|{word[::-1]})", diagonal2, overlapped=True)
            )
            print(number_r, number_c, number_d1, number_d2)
        places_to_check = self.rows + self.columns + self.diagonalsLR + self.diagonalsRL
        check_string = " ".join(place for place in places_to_check)
        return len(re.findall(f"({word}|{word[::-1]})", check_string, overlapped=True))

    def find_crossed(self, word="MAS"):
        a, b, c = word[0], word[1], word[2]
        possible_configs = [
            f"{a}.{a}.{b}.{c}.{c}",
            f"{a}.{c}.{b}.{a}.{c}",
            f"{c}.{c}.{b}.{a}.{a}",
            f"{c}.{a}.{b}.{c}.{a}",
        ]
        crossed = 0
        for k in range(self.m - 2):
            for j in range(self.n - 2):
                config = (
                    self.rows[k][j]
                    + "."
                    + self.rows[k][j + 2]
                    + "."
                    + self.rows[k + 1][j + 1]
                    + "."
                    + self.rows[k + 2][j]
                    + "."
                    + self.rows[k + 2][j + 2]
                )
                if config in possible_configs:
                    crossed += 1
        return crossed

    def __str__(self):
        return "\n".join(row for row in self.rows)


if __name__ == "__main__":

    search1 = WordSearch(test_data1)
    # print(search1.rows)
    # print(search1.columns)
    # print(search1.diagonalsLR)
    # print(search1.diagonalsRL)
    assert search1.find_word("XMAS") == 4

    search2 = WordSearch(test_data2)
    assert search2.find_word("XMAS") == test_answer

    search3 = WordSearch(test_data3)
    assert search3.find_word("XMAS") == test_answer

    with open("../input_data/04_Ceres_Search.txt", "r", encoding="utf-8") as file:
        input = file.read().strip()

    answer_search = WordSearch(input)
    answer1 = answer_search.find_word("XMAS")
    print(answer1)

    # Part 2

    assert search2.find_crossed("MAS") == test_answer2

    search4 = WordSearch(test_data4)
    assert search4.find_crossed("MAS") == test_answer2

    answer2 = answer_search.find_crossed("MAS")
    print(answer2)
