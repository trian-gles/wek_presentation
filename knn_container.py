from collections import Counter
from typing import List, Tuple


class NeighborContainer:
    def __init__(self, k: int, x: List[float], y: List[float], classes: list):
        self.k = k
        self.short_distances = [0 for _ in range(k)]
        self.short_classes = self.short_distances.copy()
        self.short_indexes = self.short_distances.copy()

        self.x = x
        self.y = y
        self.classes = classes

    def test_point(self, coor: Tuple[float, float]):
        for i in range(len(self.x)):

            x_dist = self.x[i] - coor[0]
            y_dist = self.y[i] - coor[1]
            dist = (x_dist ** 2 + y_dist ** 2) ** (1 / 2)

            if 0 in self.short_distances:

                self.add_neighbor(i, self.classes[i], dist, self.short_distances.index(0))
                continue

            max_dist = max(self.short_distances)
            if dist < max_dist:
                self.add_neighbor(i, self.classes[i], dist, self.short_distances.index(max_dist))

    def add_neighbor(self, index_in_points, cls, dist: float, i: int):
        self.short_distances[i] = dist
        self.short_classes[i] = cls
        self.short_indexes[i] = index_in_points

    def vote(self):
        counter = Counter()
        for cls in self.short_classes:
            counter[cls] += 1

        return counter.most_common(1)[0][0]

    def get_neighbor_indexes(self):
        return self.short_indexes


if __name__ == '__main__':
    nc = NeighborContainer(3, [1, 4, 6, 2], [6, 4, 8, 2], ["face", "face", "lime", "face"])
    nc.test_point((3, 8))
    print(nc.get_neighbor_indexes())
    print(nc.vote())

