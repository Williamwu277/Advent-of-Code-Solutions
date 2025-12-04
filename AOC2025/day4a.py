"""
Day 4A
For each @ grid, check all 8 directions
"""

DX = [1, 1, 1, -1, -1, -1, 0, 0]
DY = [1, -1, 0, 1, -1, 0, 1, -1]
THRESHOLD = 4

count = 0

with open("input.in", "r") as f:

    grid = []
    
    for line in f:
        grid.append(line)

    N, M = len(grid), len(grid[0])

    for i in range(N):
        for j in range(M):
            if grid[i][j] != '@': continue
            nearby = 0
            for k in range(len(DX)):
                nx, ny = DX[k] + i, DY[k] + j
                if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == '@': nearby += 1
            if nearby < THRESHOLD:
                count += 1

print(count)
