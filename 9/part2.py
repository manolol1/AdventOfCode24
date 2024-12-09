import utils

data = list(map(int, utils.load_data("task-data.txt")[0]))
# print(data)

blocks = []

def blocks_to_str():
    res = ""
    for x in blocks:
        if x[0] == -1:
            res += "." * x[1]
        else:
            res += str(x[0]) * x[1]
    return res

# convert input data into a block representation with tuples (file_id, block_size)
for i, n in enumerate(data):
    if i % 2 == 0:
        blocks.append((i // 2, n))
    else:
        blocks.append((-1, n))


# move blocks
for i in range(len(blocks) - 1, -1, -1):
    n = blocks[i]
    if n[0] == -1:
        continue
    for j in range(len(blocks)):
        m = blocks[j]
        if j >= i or m[0] != -1:
            continue
        if n[1] <= m[1]:
            blocks[j] = blocks[i]
            blocks[i] = (-1, blocks[j][1])
            if n[1] != m[1]:
                blocks.insert(j + 1, (-1, m[1] - n[1]))
            break

print(blocks)

# calculate checksum
sum = 0
pos = 0
for x in blocks:
    if x[0] != -1:
        for n in range(0, x[1]):
            sum += x[0] * pos
            pos += 1
    else:
        pos += x[1]

print(sum)

#print(sum([int(x) * i for i, x in enumerate(blocks_to_str()) if x != '.']))