# Day 12 - Garden Groups

import re
from random import choice

test_data = """AAAA
BBCD
BBCC
EEEC"""

test_answer = 140

test_data2 = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""

test_answer2 = 772

test_data3 = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

test_answer3 = 1930


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
        for i, row in enumerate(self.rows):
            for j, plant in enumerate(row):
                if plant == plant_type:
                    plant_region.append((i, j))

        return plant_region

    def test_if_connected(plant_region):
        def neighbours(plant):
            x, y = plant
            candidates = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            return [c for c in candidates if c in plant_region]

        seen = set()

        frontier = [choice(list(plant_region))]

        while not len(frontier) == 0:
            point = frontier.pop()
            seen.add(point)
            frontier.extend([n for n in neighbours(point) if not n in seen])

        if len(seen) == len(plant_region):
            return plant_region, None
        else:
            region = [plant for plant in plant_region if not plant in seen]
            return seen, region

    def perimeter_of_plant(self, plant_position, plant_type):
        perimeter = 0
        i, j = plant_position

        if i == 0:
            perimeter += 1
        elif self.rows[i - 1][j] != plant_type:
            perimeter += 1

        if i == self.m - 1:
            perimeter += 1
        elif self.rows[i + 1][j] != plant_type:
            perimeter += 1

        if j == 0:
            perimeter += 1
        elif self.rows[i][j - 1] != plant_type:
            perimeter += 1

        if j == self.n - 1:
            perimeter += 1
        elif self.rows[i][j + 1] != plant_type:
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

    def price_of_garden(self):
        price = 0
        for plant in self.plants:
            region = False
            while not region:
                area, perimeter, region = self.find_region(plant)
                # print(plant, area, perimeter)
                price += self.price_of_region(area, perimeter)

        return price


if __name__ == "__main__":

    test_garden = Garden(test_data)

    area, perimeter, region = test_garden.find_region("A")

    assert test_garden.price_of_region(area, perimeter) == 40
    assert test_garden.price_of_garden() == test_answer

    test_garden2 = Garden(test_data2)

    assert test_garden2.price_of_garden() == test_answer2

    test_garden3 = Garden(test_data3)

    # assert test_garden3.price_of_garden() == test_answer3


from random import choice
