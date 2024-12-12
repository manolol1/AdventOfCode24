import utils

field = [list(line) for line in utils.load_data("sample-data.txt")]

utils.print_matrix(field)

for i, row in enumerate(field):
    for j, col in enumerate(field[i]):
        pass