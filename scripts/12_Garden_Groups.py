# Day 12 - Garden Groups

import re
from random import choice
from collections import defaultdict

test_data = """AAAA
BBCD
BBCC
EEEC"""

test_answer = 140
test_answer_2 = 80

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
test_answer3_2 = 1206

test_data4 = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""

test_answer4 = 236

test_data5 = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""

test_answer5 = 368


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

    def test_if_connected(self, plant_region, regions=[]):

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

        regions.append(list(seen))
        if len(seen) != len(plant_region):
            region = [plant for plant in plant_region if not plant in seen]
            regions = self.test_if_connected(region, regions)

        return regions

    def perimeter_of_plant(self, plant_position, plant_type):
        region_edge = []
        perimeter = 0
        i, j = plant_position

        if i == 0:
            perimeter += 1
            region_edge.append(("row", -1.25, j))
        elif self.rows[i - 1][j] != plant_type:
            perimeter += 1
            region_edge.append(("row", (i - 1) - 0.25, j))

        if i == self.m - 1:
            perimeter += 1
            region_edge.append(("row", self.m + 0.25, j))
        elif self.rows[i + 1][j] != plant_type:
            perimeter += 1
            region_edge.append(("row", (i + 1) + 0.25, j))

        if j == 0:
            perimeter += 1
            region_edge.append(("col", -1.25, i))
        elif self.rows[i][j - 1] != plant_type:
            perimeter += 1
            region_edge.append(("col", (j - 1) - 0.25, i))

        if j == self.n - 1:
            perimeter += 1
            region_edge.append(("col", self.n + 0.25, i))
        elif self.rows[i][j + 1] != plant_type:
            perimeter += 1
            region_edge.append(("col", (j + 1) + 0.25, i))

        return perimeter, region_edge

    def perimeter_of_region(self, plant_region, plant_type):
        region_edges = defaultdict(list)
        perimeter = 0
        for position in plant_region:
            perim, region_edge = self.perimeter_of_plant(position, plant_type)
            perimeter += perim
            for edge in region_edge:
                edge_type, id1, id2 = edge
                region_edges[(edge_type, id1)].append(id2)

        return perimeter, region_edges

    def area_of_region(self, plant_region):
        return len(plant_region)

    def edges_of_region(self, region_edges):
        num_edges = 0
        for edge_coords in region_edges.values():
            edge_coords = sorted(edge_coords)
            for i, coord in enumerate(edge_coords):
                if coord != edge_coords[i - 1] + 1:
                    num_edges += 1
        return num_edges

    def price_of_region(self, plant_region, plant_type):
        area = self.area_of_region(plant_region)
        perimeter, region_edges = self.perimeter_of_region(plant_region, plant_type)
        return area * perimeter

    def discounted_price_of_region(self, plant_region, plant_type):
        area = self.area_of_region(plant_region)
        perimeter, region_edges = self.perimeter_of_region(plant_region, plant_type)
        num_edges = self.edges_of_region(region_edges)
        return area * num_edges

    def price_of_garden(self, discount=False):
        price = 0
        for plant in self.plants:
            regions = []
            plant_region = self.find_region(plant)
            all_regions = self.test_if_connected(plant_region, regions)
            for region in all_regions:
                if discount:
                    price += self.discounted_price_of_region(region, plant)
                else:
                    price += self.price_of_region(region, plant)

        return price


if __name__ == "__main__":

    test_garden = Garden(test_data)

    plant_region = test_garden.find_region("A")

    assert test_garden.price_of_region(plant_region, "A") == 40

    assert test_garden.price_of_garden() == test_answer

    test_garden2 = Garden(test_data2)

    assert test_garden2.price_of_garden() == test_answer2

    test_garden3 = Garden(test_data3)

    assert test_garden3.price_of_garden() == test_answer3

    with open("../input_data/12_Garden_Groups.txt", "r", encoding="utf-8") as file:
        input = file.read().strip()

    answer_garden = Garden(input)
    answer1 = answer_garden.price_of_garden()
    print(answer1)

    assert test_garden.price_of_garden(discount=True) == test_answer_2

    assert test_garden3.price_of_garden(discount=True) == test_answer3_2

    test_garden4 = Garden(test_data4)

    assert test_garden4.price_of_garden(discount=True) == test_answer4

    test_garden5 = Garden(test_data5)

    assert test_garden5.price_of_garden(discount=True) == test_answer5

    answer2 = answer_garden.price_of_garden(discount=True)
    print(answer2)
