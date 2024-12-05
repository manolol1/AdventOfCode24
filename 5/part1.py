import utils

data = utils.load_data("sample-data.txt")

rules = [tuple(line.split("|")) for line in data if "|" in line]
updates = [line.split(",") for line in data if "," in line]

# check if update follows all rules
def check_rules(value):
    for rule in rules:
        if value == rule[0]:
            if rule[1] not in updates or updates.index(value) > updates.index(rule[1]):
                return False
    return True

# remove incorrect updates from list
for update in updates:
    for number in update:
        if not check_rules(number):
            updates.remove(update)
            break

print(updates)

# determine sum of all page numbers in the middle of the valid updates
middle_page_numbers = [update[int(len(update) / 2) + 1] for update in updates]

print(middle_page_numbers)