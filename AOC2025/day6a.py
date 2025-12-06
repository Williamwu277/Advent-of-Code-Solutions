"""
Day 6A
2D array navigation
"""

with open("input.in", "r") as f:

    grid = []

    for line in f:

        grid.append(list(line.split()))

    N = len(grid) - 1
    M = len(grid[0])
    total = 0

    for i in range(M):

        current = 0

        for j in range(N):

            if j == 0: current = int(grid[j][i])
            else:
                current = eval(f"{current} {grid[N][i]} {grid[j][i]}")

        total += current
    
    print(total)

