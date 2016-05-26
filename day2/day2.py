f = open('./input.txt')
arr = f.read().split('\n')

# part 1
result = 0

def count_paper(lwh):
    (l, w, h) = tuple(lwh)
    sides = [l*w, w*h, h*l]
    sqft = (2*sides[0]) + (2*sides[1]) + (2*sides[2])
    return sqft + sorted(sides)[0]

# part 2
ribbon = 0

def count_ribbon(lwh):
   lwh = sorted(lwh) 
   return 2*lwh[0] + 2*lwh[1] + (lwh[0] * lwh[1] * lwh[2])

for i in arr:
    result += count_paper(list(map(int, i.split('x'))))
    ribbon += count_ribbon(list(map(int, i.split('x'))))

print(result, ribbon)
