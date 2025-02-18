def is_safe(report, order):
    """Check if the report is safe in its current form."""
    if order == 0:
        for i in range(1, len(report)):
            if (report[i] >= report[i - 1]) or abs(report[i] - report[i - 1]) < 1 or abs(report[i] - report[i - 1]) > 3:
                return False
        return True
    else:
        for i in range(1, len(report)):
            if (report[i] <= report[i - 1]) or abs(report[i] - report[i - 1]) < 1 or abs(report[i] - report[i - 1]) > 3:
                return False
        return True


def can_be_made_safe(report):
    """Check if removing one level makes the report safe."""
    for to_remove in range(len(report)):
        modified_report = report[:to_remove] + report[to_remove + 1:]
        if is_safe(modified_report, 1) or is_safe(modified_report, 0):
            return True
    return False

res = 0

# Process 6 reports
for _ in range(1000):
    line = input()
    report = [int(x) for x in line.split()]
    
    # Check if the report is safe or can be made safe
    if is_safe(report, 1) or is_safe(report, 0) or can_be_made_safe(report):
        res += 1

print(res)
