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


class WordSearch:

    def __init__(self, grid):
        self.grid = grid
        self.rows = grid.split("\n")
        self.columns = self.to_columns()
        self.size = (len(self.rows), len(self.columns))
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
        if self.size[0] == self.size[1]:
            for j in range(len(self.columns)):
                diagonal = ""
                for i in range(row, len(self.rows) - j):
                    diagonal += self.rows[i][i + j]
                self.diagonals.append(diagonal)
            for row in range(1, len(self.columns)):
                diagonal = ""
                for j in range(len(self.rows) - row):
                    diagonal += self.rows[row + j][j]
                self.diagonals.append(diagonal)

        else:
            j = 0
            diagonal = ""
            for i in range(row, len(self.rows) - j):
                diagonal += self.rows[i][i + j]
            self.diagonals.append(diagonal)
            for j in range(1, len(self.columns)):
                diagonal = ""
                for i in range(row, len(self.rows) - j + 1):
                    diagonal += self.rows[i][i + j]
                self.diagonals.append(diagonal)
            for row in range(1, len(self.columns) - 1):
                diagonal = ""
                for j in range(len(self.rows) - row):
                    diagonal += self.rows[row + j][j]
                self.diagonals.append(diagonal)

        return self.diagonals

    def to_diagonalsRL(self):
        self.diagonals = []
        row = self.size[0] - 1
        if self.size[0] == self.size[1]:
            for j in range(len(self.columns)):
                diagonal = ""
                for i in range(len(self.rows) - j):
                    if row - i < 0:
                        continue
                    diagonal += self.rows[row - i][i + j]
                self.diagonals.append(diagonal)
            for row in reversed(range(len(self.columns) - 1)):
                diagonal = ""
                for j in range(row + 1):
                    diagonal += self.rows[row - j][j]
                self.diagonals.append(diagonal)

        else:
            for j in range(len(self.columns)):
                diagonal = ""
                for i in range(len(self.rows) - j + 1):
                    if row - i < 0:
                        continue
                    diagonal += self.rows[row - i][i + j]
                self.diagonals.append(diagonal)
            for row in reversed(range(len(self.columns) - 2)):
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
    assert search3.find_word("XMAS", debug=True) == test_answer
