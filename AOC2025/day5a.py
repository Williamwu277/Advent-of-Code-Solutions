"""
Day 5A
Input looks small enough for N * M (N being number of ranges, and M being number of ids)
"""

count = 0

with open("input.in", "r") as f:

    dates = []

    for line in f:

        if line == "\n": break
        dates.append(tuple(map(int, line.split("-"))))
    
    for line in f:

        value = int(line)
        flag = False

        for pair in dates:

            if pair[0] <= value <= pair[1]: flag = True

        if flag: count += 1

print(count)
