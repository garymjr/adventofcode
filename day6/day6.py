import re

f = open('./input.txt')
arr = f.read().split('\n')
lights = [None] * 1000

for i in range(0, 1000):
    lights[i] = [0]
"""
for line in arr:
    lights = re.findall(r'(\d+,\d+)', line)
"""

print(lights)