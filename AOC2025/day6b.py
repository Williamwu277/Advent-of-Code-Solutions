"""
Day 6B
Need to process along with whitespace, so cannot split
Find the 'break point' columns of all spaces
Then for each number column go index by index
"""

with open("input.in", "r") as f:

    grid = []

    for line in f:

        grid.append(line)

    N = len(grid) - 1
    M = len(grid[0])
    break_points = [-1]

    for i in range(M):

        flag = True

        for j in range(N):

            if grid[j][i] != " ": flag = False
            
        if flag: break_points.append(i)
    
    break_points.append(M)
    total = 0

    for b in range(len(break_points) - 1):

        start, end = break_points[b] + 1, break_points[b + 1] - 1
        numbers = []

        for i in range(start, end + 1):

            number = 0

            for j in range(N):

                if grid[j][i] not in " \n": number = number * 10 + int(grid[j][i])
            
            numbers.append(str(number))

        total += eval(f" {grid[N][start]} ".join(numbers))
                
    print(total)

