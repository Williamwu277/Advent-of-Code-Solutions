"""
Day 1B
"""

cur_num = 50
count = 0

with open("input.in", "r") as f:

    for line in f:
        
        prev_num = cur_num

        diff = int(line[1:])

        # For every +- 100, it is guaranteed to go past 0 once
        count += diff // 100

        if line[0] == 'R':
            cur_num = (cur_num + diff) % 100
        else:
            cur_num = (cur_num - diff) % 100

        # Based on if the number is smaller/larger than previous value
        # We know whether or not it went past 0 (but also did not move a full cycle)
        if line[0] == 'R' and cur_num < prev_num: count += 1

        if line[0] == 'L' and (cur_num if cur_num != 0 else 100) > (prev_num if prev_num != 0 else 100): count += 1
    
print(count)
