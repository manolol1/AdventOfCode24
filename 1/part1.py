# https://adventofcode.com/2024/day/1

import utils

data = utils.load_data("task-data.txt")

# split lines from input file into two lists
list1, list2 = [list(map(int, t)) for t in zip(*((line.split("   ")) for line in data))]

list1.sort()
list2.sort()

difference = [abs(m - n) for m, n in zip(list1, list2)]

print(sum(difference))