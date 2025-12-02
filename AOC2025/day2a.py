"""
Day 2A
------
The [s, e] ranges seem to be quite small (< 100,000), so a brute force approach should work
"""

count = 0

with open("input.in", "r") as f:

    ranges = f.readline().split(',')

    for r in ranges:

        s, e = map(int, r.split('-'))

        for i in range(s, e + 1):
            
            num = str(i)
            num_len = len(num)

            if num[:num_len // 2] == num[num_len // 2:]:
                count += i

print(count)
