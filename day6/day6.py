import re

f = open('./input.txt')
arr = f.read().split('\n')
lights = [0] * 1000

# build lights list
def reset_lights():
    for i in range(0, 1000):
        lights[i] = [0] * 1000


def control_lights(instruction, light_set):
    set1 = list(map(int, light_set[0].split(',')))
    set2 = list(map(int, light_set[1].split(',')))
    if instruction == "on":
        for i in range(set1[0], set2[0]+1):
            for j in range(set1[1], set2[1]+1):
                lights[i][j] = 1
    elif instruction == "off":
        for i in range(set1[0], set2[0]+1):
            for j in range(set1[1], set2[1]+1):
                lights[i][j] = 0
    elif instruction == "toggle":
        for i in range(set1[0], set2[0]+1):
            for j in range(set1[1], set2[1]+1):
                if lights[i][j] == 0:
                    lights[i][j] = 1
                else:
                    lights[i][j] = 0

def count_lights():
    count = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            if lights[i][j] == 1:
                count += 1
    return count

def control_brightness(instruction, light_set):
    set1 = list(map(int, light_set[0].split(',')))
    set2 = list(map(int, light_set[1].split(',')))
    if instruction == "on":
        for i in range(set1[0], set2[0]+1):
            for j in range(set1[1], set2[1]+1):
                lights[i][j] += 1
    elif instruction == "off":
        for i in range(set1[0], set2[0]+1):
            for j in range(set1[1], set2[1]+1):
                if lights[i][j] >= 1:
                    lights[i][j] -= 1
    elif instruction == "toggle":
        for i in range(set1[0], set2[0]+1):
            for j in range(set1[1], set2[1]+1):
                lights[i][j] += 2

def count_brightness():
    brightness = 0
    for i in range(0, 1000):
        brightness += sum(lights[i])
    return brightness

reset_lights()
for line in arr:
    instruction = re.findall(r'(on|off|toggle)', line)[0]
    light_set = re.findall(r'(\d+,\d+)', line)
    control_lights(instruction, light_set)

print(count_lights())

reset_lights()
for line in arr:
    instruction = re.findall(r'(on|off|toggle)', line)[0]
    light_set = re.findall(r'(\d+,\d+)', line)
    control_brightness(instruction, light_set)

print(count_brightness())