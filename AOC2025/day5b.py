"""
Day 5B
The id ranges are extremely large values, so we need to iterate through the ranges rather than values
Note that you can just merge the ranges and count the remaining disjoint ranges 
"""

with open("input.in", "r") as f:

    id_ranges = []

    for line in f:

        if line == "\n": break
        id_ranges.append(tuple(map(int, line.split("-"))))

id_ranges.sort()
begin, end = id_ranges[0][0], id_ranges[0][1]
count = 0

for id_range in id_ranges:

    if id_range[0] > end:

        count += end - begin + 1
        begin = id_range[0]
        end = id_range[1]
    
    else:

        end = max(end, id_range[1])
    
count += end - begin + 1
print(count)
