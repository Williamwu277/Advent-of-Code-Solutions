"""
Day 3A
------
Consider each index as the second digit, keep track of the biggest first digit
"""

total = 0

with open("input.in", "r") as f:

    for line in f:

        batteries = line.rstrip()
        max_prev_digit, best = -1, -1

        for nxt in batteries:

            battery = max_prev_digit * 10 + int(nxt)
            max_prev_digit = max(max_prev_digit, int(nxt))
            best = max(battery, best)
            
        total += best

print(total)
