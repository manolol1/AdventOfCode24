import utils

lines = utils.load_data("task-data.txt")

word_matrix = [list(line) for line in lines]


def count_x_mas_occurrences(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    # check if position is inside bounds of matrix
    def is_in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check(x, y, letter):
        return is_in_bounds(x, y) and matrix[x][y] == letter

    def check_patterns(i, j):
        # every possible combination of patterns the X-MAS could be in
        patterns = [
            [(i-1, j-1, 'M'), (i+1, j+1, 'S'), (i+1, j-1, 'M'), (i-1, j+1, 'S')],
            [(i-1, j+1, 'M'), (i+1, j-1, 'S'), (i+1, j+1, 'M'), (i-1, j-1, 'S')],
            [(i-1, j-1, 'M'), (i+1, j+1, 'S'), (i-1, j+1, 'M'), (i+1, j-1, 'S')],
            [(i+1, j-1, 'M'), (i-1, j+1, 'S'), (i+1, j+1, 'M'), (i-1, j-1, 'S')]
        ]
        for pattern in patterns:
            if all(check(x, y, letter) for x, y, letter in pattern):
                return True
        return False

    # find all X-MAS patterns
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'A' and check_patterns(i, j):
                count += 1

    return count


occurrences = count_x_mas_occurrences(word_matrix)

print(occurrences)
