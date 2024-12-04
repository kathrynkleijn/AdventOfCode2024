# Day 4 - Ceres Search

test_data1 = """..X...
.SAMX.
.A..A.
XMAS.S
.X...."""


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
        row = 0
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

    def __str__(self):
        return "\n".join(row for row in self.rows)


if __name__ == "__main__":
    search1 = WordSearch(test_data1)
    # print(search1.rows)
    # print(search1.columns)
    print(search1.diagonals)
