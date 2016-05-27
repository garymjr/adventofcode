f = open("./input.txt")
lines = f.readlines()
str_literal = 0
str_memory = 0
num_codes = 0

for line in lines:
    line = line.rstrip()
    str_literal += len(line)
    str_memory += len(eval(line))
    num_codes += line.count("\\") + line.count("\"") + 2

print(str_literal - str_memory)
print(num_codes)