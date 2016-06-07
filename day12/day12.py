import json

f = open("./input.json")
json_input = json.loads(f.read())

def solve1(item):
    if type(item) == int:
        yield item
    elif type(item) == type([]):
        for x in item:
            for y in solve1(x):
                yield y
    elif type(item) == type({}):
        for x, y in item.items():
            for z in solve1(y):
                yield z

def solve2(item):
    if type(item) == int:
        yield item
    elif type(item) == type([]):
        for x in item:
            for y in solve2(x):
                yield y
    elif type(item) == type({}):
        shouldYield = True
        for x, y in item.items():
            if x == "red" or y == "red":
                shouldYield = False

        for x, y in item.items():
            for z in solve2(y):
                if shouldYield:
                    yield z

part1 = sum(list(solve1(json_input)))
print(part1)

part2 = 0
for y in solve2(json_input):
    part2 += y
print(part2)
