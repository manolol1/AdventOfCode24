# bruteforce "algorithm" with time complexity of O(n^3) (if I understand this correctly), took about 30s with task-data
# I might look into more efficient ways with graphs (or something like that) soon.

import utils
import sys

# increasing the recursion limit is probably not a good idea, but I wanted to try this with recursion, so I do it anyway.
sys.setrecursionlimit(200000)

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
            initial_guard_pos = [row, col]

def move(n):
    """
    Move the guard forward in the current direction, if possible.
    If the path is blocked by an obstacle, turn right.
    If an endless loop is detected, return true
    """
    global guard_direction, guard_pos

    if n <= 0:
        return True

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
        return move(n - 1)
    return False

possibilities = 0

# count possibilities
for row in range(map_bounds[0]):
    for col in range(map_bounds[1]):
        if map[row][col] != '#':
            map[row][col] = '#'
            if move(10000):
                possibilities += 1
            map[row][col] = 'o'
            guard_pos[0], guard_pos[1] = initial_guard_pos[0], initial_guard_pos[1]
            guard_direction = directions[3]

print(possibilities)