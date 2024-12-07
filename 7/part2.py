import operator
import itertools

import utils

data = utils.load_data("task-data.txt")

equations = [(int(e.split(':')[0]), list(map(int, e.split(':')[1].split()))) for e in data]


def concat(a, b):
    """Concatenate two integers like strings"""
    return int(str(a) + str(b))

def get_possible_results(values):
    operators = [operator.add, operator.mul, concat]

    possible_results = []

    for ops in itertools.product(operators, repeat=len(values)-1): # for every possible combination of operators ("cartesian product")
        result = values[0]
        # apply current combination of operators to values
        for i, op in enumerate(ops):
            result = op(result, values[i+1])
        possible_results.append(result)

    return possible_results

sum = 0

for e in equations:
    if e[0] in get_possible_results(e[1]):
        sum += e[0]

print(sum)