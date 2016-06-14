import re

with open('input.txt') as f:
    lines = f.read().split('\n')[:-1]

original = lines.pop()

# part 1
replacements = []
for i in lines[:-1]:
    m = re.findall(r'(\S+) => (\S+)', i)
    replacements.append(m[0])

molecules = set()
for i, j in replacements:
    for k in range(len(original)):
        if original[k:k+len(i)] == i:
            l = original[:k] + j + original[k+len(i):]
            molecules.add(l)

print(len(molecules))

# part 2
original = original[::-1]
reps = {m[1][::-1]: m[0][::-1] for m in re.findall(r'(\w+) => (\w+)', "\n".join(lines))}

def rep(x):
    return reps[x.group()]

count = 0
while original != 'e':
    original = re.sub('|'.join(reps.keys()), rep, original, 1)
    count += 1
print(count)
