# Day 12 - Garden Groups

import re

test_data = """AAAA
BBCD
BBCC
EEEC"""


class Garden:

    def __init__(self, grid):
        self.grid = grid
        self.rows = self.to_rows()
        self.columns = self.to_columns()
        self.m = len(self.rows)
        self.n = len(self.columns)
        self.size = (self.m, self.n)
        self.plants = self.find_plants()

    def to_rows(self):
        rows = []
        lines = self.grid.split("\n")
        for line in lines:
            rows.append([char for char in line])
        return rows

    def to_columns(self):
        columns = []
        for col in range(len(self.rows[0])):
            columns.append("".join(row[col] for row in self.rows))
        return columns

    def find_plants(self):
        filtered = re.sub(r"[^a-zA-Z]", "", self.grid)
        return list(set(filtered))

    def find_region(self, plant_type):
        plant_region = []
        for row in self.rows:
            new_row = [plant if plant == plant_type else "." for plant in row]
            plant_region.append(new_row)
        return plant_region

    def perimeter_of_plant(self, plant_region, plant_position):
        perimeter = 0
        i, j = plant_position

        if i == 0:
            perimeter += 1
        elif plant_region[i - 1][j] == ".":
            perimeter += 1

        if i == self.m - 1:
            perimeter += 1
        elif plant_region[i + 1][j] == ".":
            perimeter += 1

        if j == 0:
            perimeter += 1
        elif plant_region[i][j - 1] == ".":
            perimeter += 1

        if j == self.n - 1:
            perimeter += 1
        elif plant_region[i][j + 1] == ".":
            perimeter += 1

        return perimeter

    def perimeter_of_region(self, plant_region):
        plant_positions = []
        for i, row in enumerate(plant_region):
            for j, plant in enumerate(row):
                if plant != ".":
                    plant_positions.append((i, j))
        perimeter = 0
        for position in plant_positions:
            perimeter += self.perimeter_of_plant(plant_region, position)

        return perimeter

    def area_of_region(self, plant_region):
        area = 0
        for row in plant_region:
            for plant in row:
                if plant != ".":
                    area += 1
        return area

    def price_of_region(self, plant_region):
        area = self.area_of_region(plant_region)
        perimeter = self.perimeter_of_region(plant_region)
        return area * perimeter


if __name__ == "__main__":

    test_garden = Garden(test_data)
    plant_region = test_garden.find_region("A")
    assert test_garden.price_of_region(plant_region) == 40
