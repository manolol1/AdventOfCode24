# https://adventofcode.com/2024/day/1

import utils

data = utils.load_data("task-data.txt")

# split lines from input file into two lists
list1, list2 = [list(map(int, t)) for t in zip(*((line.split("   ")) for line in data))]

similarity_score = sum(list2.count(i) * i for i in list1)

print(similarity_score)
