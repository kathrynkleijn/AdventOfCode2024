# Day 8 - Resonant Collinearity

import re
import itertools

test_data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
test_answer = 14
test_answer2 = 34

test_data2 = """..........
...#......
..........
....a.....
..........
.....a....
..........
......#...
..........
.........."""

test_data3 = """..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......#...
..........
.........."""

test_data4 = """..........
..........
..........
....a.....
........a.
.....a....
..........
......A...
..........
.........."""

test_data5 = """T.........
...T......
.T........
..........
..........
..........
..........
..........
..........
.........."""


class AntennaMap:

    def __init__(self, map):
        self.map = map
        self.rows = map.split("\n")
        self.columns = self.to_columns()
        self.m = len(self.rows)
        self.n = len(self.columns)
        self.size = (self.m, self.n)
        self.frequencies = self.unique_frequency()
        self.antennas = self.find_positions()
        self.nodes = self.find_antinodes()
        self.harmonic_nodes = self.find_antinodes_with_harmonics()

    def to_columns(self):
        self.columns = []
        for col in range(len(self.rows[0])):
            self.columns.append("".join(row[col] for row in self.rows))
        return self.columns

    def unique_frequency(self):
        filtered = re.sub(r"[^a-zA-Z\d+]", "", self.map)
        return list(set(filtered))

    def find_positions(self):
        antennas = {frequency: [] for frequency in self.frequencies}
        for frequency in self.frequencies:
            for num, row in enumerate(self.rows):
                points = [(num, m.start()) for m in re.finditer(frequency, row)]
                antennas[frequency].extend(points)
        return antennas

    def find_antinodes(self):
        nodes = []
        for antennas in self.antennas.values():
            antenna_pairs = [pair for pair in itertools.combinations(antennas, 2)]
            for pair in antenna_pairs:
                difference = [(y - x) for x, y in zip(pair[0], pair[1])]
                nodes.extend(
                    [
                        (pair[0][0] - difference[0], pair[0][1] - difference[1]),
                        (pair[1][0] + difference[0], pair[1][1] + difference[1]),
                    ]
                )
        return [(x, y) for (x, y) in nodes if 0 <= x < self.n and 0 <= y < self.m]

    def num_of_unique_antinodes(self, harmonic=False):
        if harmonic:
            nodes = self.harmonic_nodes
        else:
            nodes = self.nodes
        return len(set(nodes))

    def find_antinodes_with_harmonics(self):
        nodes = []
        for antennas in self.antennas.values():
            nodes.extend(antennas)
            antenna_pairs = [pair for pair in itertools.combinations(antennas, 2)]
            for pair in antenna_pairs:
                difference = [(y - x) for x, y in zip(pair[0], pair[1])]
                difference_multiples = [difference]
                i = 2
                diff_mult = [diff * i for diff in difference]
                while abs(diff_mult[0]) < self.m and abs(diff_mult[1]) < self.n:
                    difference_multiples.append([diff * i for diff in difference])
                    i += 1
                    diff_mult = [diff * i for diff in difference]
                for diff in difference_multiples:
                    nodes.extend(
                        [
                            (pair[0][0] - diff[0], pair[0][1] - diff[1]),
                            (pair[1][0] + diff[0], pair[1][1] + diff[1]),
                        ]
                    )
        return [(x, y) for (x, y) in nodes if 0 <= x < self.n and 0 <= y < self.m]


if __name__ == "__main__":

    test_map = AntennaMap(test_data)

    assert test_map.frequencies == ["0", "A"] or ["A", "0"]
    assert test_map.antennas == {
        "0": [(1, 8), (2, 5), (3, 7), (4, 4)],
        "A": [(5, 6), (8, 8), (9, 9)],
    }

    test_map2 = AntennaMap(test_data2)
    assert test_map2.nodes == [(1, 3), (7, 6)]

    test_map3 = AntennaMap(test_data3)
    assert test_map3.nodes == [(2, 0), (1, 3), (7, 6), (6, 2)]

    test_map4 = AntennaMap(test_data4)
    assert test_map4.nodes == [(2, 0), (1, 3), (7, 6), (6, 2)]

    assert test_map.num_of_unique_antinodes() == test_answer

    with open(
        "../input_data/08_Resonant_Collinearity.txt", "r", encoding="utf-8"
    ) as file:
        input = file.read().strip()

    answer_map = AntennaMap(input)
    answer1 = answer_map.num_of_unique_antinodes()
    print(answer1)

    test_map5 = AntennaMap(test_data5)
    assert set(test_map5.harmonic_nodes) == set(
        [(0, 0), (0, 5), (1, 3), (2, 1), (2, 6), (3, 9), (4, 2), (6, 3), (8, 4)]
    )

    assert test_map.num_of_unique_antinodes(harmonic=True) == test_answer2

    answer2 = answer_map.num_of_unique_antinodes(harmonic=True)
    print(answer2)
