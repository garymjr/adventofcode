import sys
import itertools

f = open('./input.txt')
lines = f.read().split("\n")

people = ["Me"]
relations = {}

for line in lines:
    line = line.split()
    if line[0] not in people:
        people.append(line[0])
        relations[line[0] + "-Me"] = 0
        relations["Me-" + line[0]] = 0
    amt = int(line[3])
    if line[2] == "lose":
        amt = -amt
    relation = line[0] + "-" + line[-1].strip(".")
    relations[relation] = amt

optimal = -(sys.maxsize)
for x in itertools.permutations(people):
    total = 0

    for k,v in enumerate(x):
        if k == 0:
            total += relations[v + "-" + x[-1]]
            total += relations[v + "-" + x[1]]
        elif k == len(x) - 1:
            total += relations[v + "-" + x[0]]
            total += relations[v + "-" + x[-2]]
        else:
            total += relations[v + "-" + x[k+1]]
            total += relations[v + "-" + x[k-1]]
    optimal = max(total, optimal)

print(optimal)
