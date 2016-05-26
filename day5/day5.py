import re

f = open('./input.txt')
arr = f.read().split('\n')

# part 1
nice_strings = 0
def part1_filter(word):
    match = re.findall(r'[aeiou]', word)
    if  len(match) < 3:
        return False
    elif re.search(r'(.)\1+', word) == None:
        return False
    elif re.search(r'(ab|cd|pq|xy)', word) != None:
        return False

    return True

# part 2
nice_strings2 = 0
def part2_filter(word):
    if re.search(r'(..).*\1', word) == None:
        return False
    elif re.search(r'(.).\1', word) == None:
        return False

    return True

for word in arr:
    if part1_filter(word):
        nice_strings += 1
    if part2_filter(word):
        nice_strings2 += 1

print(nice_strings, nice_strings2)
