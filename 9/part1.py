import utils

data = list(map(int, utils.load_data("task-data.txt")[0]))
#print(data)

blocks = list()

# convert input data into a block representation
for i, n in enumerate(data):
    if i % 2 == 0:
        blocks.extend([i // 2 for _ in range(n)])
    else:
        blocks.extend([-1 for _ in range(n)])

#print(blocks)

# move blocks
for i, n in enumerate(blocks):
    if n == -1:
        last = -1
        while last == -1:
            last = blocks.pop()
        blocks[i] = last

#print(blocks)

print(sum([n * i for i, n in enumerate(blocks)]))