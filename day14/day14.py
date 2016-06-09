import sys

reindeer = {}
distances = {}
flying = {}
points = {}

with open('input.txt') as f:
    arr = f.read().split('\n')[0:-1]
    for a in arr:
        a = a.split()
        reindeer[a[0]] = [int(a[3]), int(a[6]), int(a[-2])]
        distances[a[0]] = 0
        points[a[0]] = 0
        flying[a[0]] = [True, 0]

for _ in range(2503):
    for k in reindeer:
        if flying[k][0] is True and flying[k][1] == reindeer[k][1]:
            flying[k][0] = False
            flying[k][1] = 0
        elif flying[k][0] is False and flying[k][1] == reindeer[k][2]:
            flying[k][0] = True
            flying[k][1] = 0
        if flying[k][0] is True:
            distances[k] += reindeer[k][0]
        flying[k][1] += 1

    max_distance = 0
    arr = []
    for k,v in distances.items():
        if v > max_distance:
            max_distance = v
            arr = [k]
        elif v == max_distance:
            arr.append(k)

    for k in arr:
        points[k] += 1

print(max(distances.values()))
print(max(points.values()))
