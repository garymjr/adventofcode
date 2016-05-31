import sys
from collections import defaultdict
from itertools import permutations

f = open ("./input.txt")

min_distance = sys.maxsize
max_distance = -min_distance - 1
lines = f.readlines()
distances = defaultdict(dict)

for line in lines:
    line = line.split()
    weight = int(line[4])
    distances[line[0]][line[2]] = weight
    distances[line[2]][line[0]] = weight

for route in permutations(distances.keys()):
    tmp = 0
    for x, y in zip(route, route[1:]):
        tmp += distances[x][y]
    min_distance = min(min_distance, tmp)
    max_distance = max(max_distance, tmp)

print(min_distance)
print(max_distance)
