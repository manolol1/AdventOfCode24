import utils

lines = utils.load_data("task-data.txt")

word_matrix = [list(line) for line in lines]

def count_occurrences(word, matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    word_len = len(word)
    count = 0

    # possible directions to check in
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (1, 1),  # down-right
        (1, -1),  # down-left
        (0, -1),  # left
        (-1, 0),  # up
        (-1, 1),  # up-right
        (-1, -1)  # up-left
    ]

    # check if position is inside bounds of matrix
    def is_in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    # check if words exists at current position and direction
    def search_from(x, y, direction):
        for k in range(word_len):
            check_x = x + k * direction[0]
            check_y = y + k * direction[1]

            if not is_in_bounds(check_x, check_y) or matrix[check_x][check_y] != word[k]:
                return False

        return True

    # check for word on every position and in every direction
    for i in range(rows):
        for j in range(cols):
            for direction in directions:
                if search_from(i, j, direction):
                    count += 1

    return count


occurrences = count_occurrences("XMAS", word_matrix)

print(occurrences)