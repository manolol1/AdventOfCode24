import utils

hiking_map = [list(map(int, list(line))) for line in utils.load_data("task-data.txt")]

utils.print_matrix(hiking_map)

directions = [
        (0, 1),  # right
        (1, 0),  # down
        (0, -1),  # left
        (-1, 0),  # up
    ]

total_score = 0
hiker = (0, 0)

# check if a move is possible
def is_possible(hiker, direction):
    next_tile = (hiker[0] + direction[0], hiker[1] + direction[1])
    if next_tile[0] < 0 or next_tile[0] >= len(hiking_map):
        return False
    if next_tile[1] < 0 or next_tile[1] >= len(hiking_map[next_tile[0]]):
        return False
    return hiking_map[next_tile[0]][next_tile[1]] == hiking_map[hiker[0]][hiker[1]] + 1

# find all possible paths from a given trailhead
def find_paths(hiker, local_score=0, found_tops=None): # the only change for solving part 2 was removing one check here :D
    if found_tops is None:
        found_tops = set()

    # check if top is found
    if hiking_map[hiker[0]][hiker[1]] == 9 and hiker:
        found_tops.add(hiker)
        return local_score + 1

    for direction in directions:
        if is_possible(hiker, direction):
            next_tile = (hiker[0] + direction[0], hiker[1] + direction[1])
            local_score = find_paths(next_tile, local_score, found_tops) # backtracking
    return local_score

# Iterate over the map to find all trailheads and calculate their scores
for row in range(len(hiking_map)):
    for col in range(len(hiking_map[row])):
        if hiking_map[row][col] == 0:
            hiker = (row, col)
            trailhead_score = find_paths(hiker)
            print(f"Trailhead at {hiker} has score {trailhead_score}")
            total_score += trailhead_score

print(total_score)