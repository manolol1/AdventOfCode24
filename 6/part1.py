import utils
import sys

# increasing the recursion limit is probably not a good idea, but I wanted to try this with recursion, so I do it anyway.
sys.setrecursionlimit(10000)

map = utils.load_data("task-data.txt")
map = [list(row) for row in map]  # Convert each row to a list of characters
map_bounds = (len(map), len(map[0]))

# possible directions the guard can be facing
directions = [
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
    (-1, 0),  # up
]

guard_pos = [0, 0]
guard_direction = directions[3]

for row in range(map_bounds[0]):
    for col in range(map_bounds[1]):
        if map[row][col] == '^':
            guard_pos = [row, col]

print(map)

def move():
    """
    Move the guard forward in the current direction, if possible.
    If the path is blocked by an obstacle, turn right,
    """
    global guard_direction, guard_pos

    next_row = guard_pos[0] + guard_direction[0]
    next_col = guard_pos[1] + guard_direction[1]

    if 0 <= next_row < map_bounds[0] and 0 <= next_col < map_bounds[1]: # check if next move would still be in bounds
        if map[next_row][next_col] != '#':
            guard_pos[0] = next_row
            guard_pos[1] = next_col
            row, col = guard_pos
            map[row][col] = 'X'
        else:
            guard_direction = directions[(directions.index(guard_direction) + 1) % len(directions)]
        move()

# move guard until it left the map
move()

print(map)

# count visited tiles
visited_tiles = sum(row.count('X') for row in map)

print(visited_tiles)