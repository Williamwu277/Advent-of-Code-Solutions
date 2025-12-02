"""
Day 2B
"""

count = 0

with open("input.in", "r") as f:

    ranges = f.readline().split(',')

    for r in ranges:

        s, e = map(int, r.split('-'))

        for i in range(s, e + 1):
            
            num = str(i)
            num_len = len(num)

            # Check possible repeat length
            for j in range(1, num_len):

                if num == num[:j] * (num_len // j):
                    count += i
                    break

print(count)
