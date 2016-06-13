with open('input.txt') as f:
    grid = f.read().split('\n')[:-1]
    for i in range(len(grid)):
        grid[i] = list(grid[i])

def create_snapshot(grid):
    if isinstance(grid, list):
        return list(map(create_snapshot, grid))
    return grid

def check_light(grid, row, col):
    if row < 0 or col < 0:
        return None

    try:
        light = grid[row][col]
        return light
    except:
        return None

def toggle_light(grid, row, col):
    corners = [(0, 0), (0, 99), (99, 99), (99, 0)]
    if (row, col) in corners:
        return '#'

    current_light = grid[row][col]
    status = [0] * 8
    if check_light(grid, row - 1, col - 1) == '#':
        status[0] = 1
    if check_light(grid, row - 1, col) == '#':
        status[1] = 1
    if check_light(grid, row - 1, col + 1) == '#':
        status[2] = 1
    if check_light(grid, row, col + 1) == '#':
        status[3] = 1
    if check_light(grid, row + 1, col + 1) == '#':
        status[4] = 1
    if check_light(grid, row + 1, col) == '#':
        status[5] = 1
    if check_light(grid, row + 1, col - 1) == '#':
        status[6] = 1
    if check_light(grid, row, col - 1) == '#':
        status[7] = 1

    if current_light == '#' and sum(status) not in [2, 3]:
        current_light = '.'
    elif current_light == '.' and sum(status) == 3:
        current_light = '#'
    return current_light

def animate_lights(grid):
    snapshot = create_snapshot(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = toggle_light(snapshot, i, j)
    return grid

for _ in range(100):
    grid = animate_lights(grid)

count = 0
for x in grid:
    for y in x:
        if y == '#':
            count += 1

print(count)
