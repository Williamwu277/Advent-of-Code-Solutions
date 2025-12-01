"""
Day 1A
"""

cur_num = 50
count = 0

with open("input.in", "r") as f:

    for line in f:

        if line[0] == 'R':
            cur_num = (cur_num + int(line[1:])) % 100
        else:
            cur_num = (cur_num - int(line[1:])) % 100
    
        if cur_num == 0:
            count += 1
    
print(count)
