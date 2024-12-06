import utils

data = utils.load_data("task-data.txt")

rules = [tuple(line.split("|")) for line in data if "|" in line]
updates = [line.split(",") for line in data if "," in line]


# check if update follows all rules and if not, fix it
def check_rules(update):
    for rule in rules:
        for value in update:
            if value == rule[0] and rule[1] in update:
                if update.index(value) > update.index(rule[1]):
                    print(update, " breaks rule ", rule)
                    return False
    return True

print(updates)
# move invalid updates into new list
invalid_updates = []
for update in updates:
    if not check_rules(update):
        invalid_updates.append(update)

print(invalid_updates)

# fix update once
def fix_update(update):
    fixed = False
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            index1 = update.index(rule[0])
            index2 = update.index(rule[1])
            if index1 > index2:
                update[index1], update[index2] = update[index2], update[index1]
                fixed = True
    return fixed

# fix updates until no more changes are needed
for update in invalid_updates:
    while fix_update(update):
        continue

# determine sum of all page numbers in the middle of the previously invalid updates
middle_page_numbers = [int(update[int(len(update) / 2)]) for update in invalid_updates]

print(middle_page_numbers)
print(sum(middle_page_numbers))