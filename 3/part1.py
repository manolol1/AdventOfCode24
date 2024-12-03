import utils
import re

data = "".join(utils.load_data("task-data.txt"))

mul_instructions = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", data)

#print(mul_instructions)

sum = 0

for instruction in mul_instructions:
    factors = [int(x) for x in re.findall(r"[0-9]{1,3}", instruction)]
    sum += factors[0] * factors[1]

print(sum)