f = open('./input.txt')
arr = list(f.read())

# part 1
def run_part1():
    cur_pos = (0, 0)
    santa_pos = [cur_pos]

    for i in arr:
        lon, lat = cur_pos
        if i == '^': lon += 1
        elif i == 'v': lon -= 1
        elif i == '>': lat += 1
        else: lat -= 1

        cur_pos = (lon, lat)
        santa_pos.append(cur_pos)

    print(len(set(santa_pos)))


def run_part2():
    cur_pos = (0, 0)
    robo_pos = (0, 0)
    santa_pos = [cur_pos]

    for i in arr:
        lon, lat = cur_pos
        if i == '^': lon += 1
        elif i == 'v': lon -= 1
        elif i == '>': lat += 1
        else: lat -= 1

        cur_pos = (lon, lat)
        santa_pos.append(cur_pos)
        cur_pos, robo_pos = (robo_pos, cur_pos)

    print(len(set(santa_pos)))


run_part1()
run_part2()