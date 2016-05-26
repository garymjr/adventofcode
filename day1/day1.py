f = open('./input.txt')
arr = list(f.read())
# part 1
result = 0
# part 2
in_basement = False
steps = 0

for i in arr:
    # part 1
    if i == '(':
        result += 1
    else:
        result -= 1
    # part 2
    if in_basement == False:
        steps += 1
        if result < 0:
            in_basement = True


print(result, steps)