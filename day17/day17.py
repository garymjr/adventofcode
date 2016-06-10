from itertools import combinations
from collections import defaultdict

with open('input.txt') as f:
    containers = list(map(int, f.read().split('\n')[:-1]))

counts = defaultdict(int)
for i in range(len(containers)):
    for j in combinations(containers, i):
        if sum(j) == 150:
            counts[i] += 1
print(sum(counts.values()))
print(counts[min(counts.keys())])
