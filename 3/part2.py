import utils
import re

data = "".join(utils.load_data("task-data.txt"))

instructions = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", data)

print(instructions)

sum = 0
mul_enabled = True

for instruction in instructions:
    if instruction == "don't()":
        mul_enabled = False
    elif instruction == "do()":
        mul_enabled = True
    else:
        if mul_enabled:
            factors = [int(x) for x in re.findall(r"[0-9]{1,3}", instruction)]
            sum += factors[0] * factors[1]

print(sum)