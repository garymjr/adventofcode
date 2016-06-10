with open('input.txt') as f:
    lines = f.read().split('\n')[:-1]

aunts = []
compounds = ['children', 'cats', 'samoyeds', 'pomeranians', 'akitas', 'vizslas', 'goldfish', 'trees', 'cars', 'perfumes']
matching_aunt = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

for line in lines:
    aunt = {}
    line = line.split()
    for i in range(len(line)):
        for c in compounds:
            if c in line[i]:
                aunt[c] = int(line[i+1].replace(',',''))
    aunts.append(aunt)

for i in range(len(aunts)):
    is_match = True
    for k in matching_aunt:
        if k not in aunts[i].keys() or aunts[i][k] == matching_aunt[k]:
            continue
        elif k in ['cats', 'trees'] and aunts[i][k] > matching_aunt[k]:
            continue
        elif k in ['pomeranians', 'goldfish'] and aunts[i][k] < matching_aunt[k]:
            continue
        else:
            is_match = False
    if is_match == True:
        print(i+1)