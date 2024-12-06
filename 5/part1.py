import utils

data = utils.load_data("task-data.txt")

rules = [tuple(line.split("|")) for line in data if "|" in line]
updates = [line.split(",") for line in data if "," in line]

# check if update follows all rules
def check_rules(update):
    for rule in rules:
        for value in update:
            if value == rule[0] and rule[1] in update:
                if update.index(value) > update.index(rule[1]):
                    print(update, " breaks rule ", rule)
                    return False
    return True

print(updates)
# move valid updates into new list
valid_updates = []
for update in updates:
    if check_rules(update):
        valid_updates.append(update)

print(updates)

# determine sum of all page numbers in the middle of the valid updates
middle_page_numbers = [int(update[int(len(update) / 2)]) for update in valid_updates]

print(middle_page_numbers)
print(sum(middle_page_numbers))