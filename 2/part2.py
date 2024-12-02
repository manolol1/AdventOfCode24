import utils

def is_report_safe(report):
    previous = report[0]
    increasing = report[0] < report[1]

    print(report)

    for n in report[1:]:
        difference = abs(n - previous)
        if increasing:
            if n < previous or difference not in range(1, 4):
                return False
        else:
            if n > previous or difference not in range(1, 4):
                return False
        previous = n
    return True

def is_report_safe_damper(report):
    if is_report_safe(report):
        return True

    for i in range(len(report)):
        if is_report_safe(report[:i] + report[i+1:]):
            return True

    return False

reports = utils.load_data("task-data.txt")
safe = 0

for report in reports:
    if is_report_safe_damper([int(x) for x in report.split(" ")]):
        safe += 1

print(safe)