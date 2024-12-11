import utils

blinks = 25

stones = list(map(int, utils.load_data("task-data.txt")[0].split()))

print(stones)

for blink in range(blinks):
    new_stones = []
    for i in range(len(stones)):
        stone = stones[i]
        stone_str = str(stone)

        if stone == 0:
            new_stones.append(1)
        elif len(stone_str) % 2 == 0:
            new_stones.append(int(stone_str[:len(stone_str) // 2]))
            new_stones.append(int(stone_str[len(stone_str) // 2:]))
        else:
            new_stones.append(stone * 2024)
    stones = new_stones
    #print(stones)
    print(blink)

print(len(stones))