# improved version of part1, using (default)dict to only store amount of stones, because the order doesn't matter

from collections import defaultdict

import utils

blinks = 75

stone_input = list(map(int, utils.load_data("task-data.txt")[0].split()))
stone_set = set(stone_input)

stones = {stone: stone_input.count(stone) for stone in stone_set}

for blink in range(blinks):
    new_stones = defaultdict(int)
    for stone in stones:
        stone_str = str(stone)
        stone_count = stones[stone]

        if stone == 0:
            new_stones[1] += stone_count
        elif len(stone_str) % 2 == 0:
            new_stones[int(stone_str[:len(stone_str) // 2])] += stone_count
            new_stones[int(stone_str[len(stone_str) // 2:])] += stone_count
        else:
            new_stones[2024 * stone] += stone_count
    stones = new_stones

print(sum(stones.values()))