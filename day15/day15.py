ingredients = {}

with open('input.txt') as f:
    lines = f.read().split('\n')[:-1]
    for l in lines:
        l = l.split()
        ingredients[l[0]] = [
            int(l[2][:-1]), # capacity
            int(l[4][:-1]), # durability
            int(l[6][:-1]), # flavor
            int(l[8][:-1]), # texture
            int(l[10])      # calories
        ]

scores = []
max_score = 0
for i in range(101):
    for j in range(101 - i):
        for k in range(101 - i - j):
            for l in range(101 - i - j - k):
                score = 1
                totals = []
                for x in range(5):
                    total = ingredients['Sprinkles:'][x] * i + \
                    ingredients['Butterscotch:'][x] * j + \
                    ingredients['Chocolate:'][x] * k + \
                    ingredients['Candy:'][x] * l
                    if total < 0:
                        total = 0
                    totals.append(total)
                for t in range(4):
                    score *= totals[t]
                if score > 0:
                    scores.append(score)
                if totals[4] == 500 and (i+j+k+l) == 100:
                    max_score = max(max_score, score)

print(max(scores))
print(max_score)