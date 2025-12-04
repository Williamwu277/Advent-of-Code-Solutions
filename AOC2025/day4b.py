"""
Day 4B
Kind of like a topological sort
"""
from collections import deque

DX = [1, 1, 1, -1, -1, -1, 0, 0]
DY = [1, -1, 0, 1, -1, 0, 1, -1]
THRESHOLD = 4

count = 0

with open("input.in", "r") as f:

    # Build the grid
    grid = []
    for line in f:
        grid.append(list(line))

    N, M = len(grid), len(grid[0])
    queue = deque()
    visited = set()
    
    # Helper function to count surrounding @'s
    def check(x, y):
        nearby = 0
        for i in range(len(DX)):
            nx, ny = DX[i] + x, DY[i] + y
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == '@': nearby += 1
        return nearby
    
    # Find the initial nodes to visit
    for i in range(N):
        for j in range(M):
            if grid[i][j] != '@': continue
            if check(i, j) < THRESHOLD:
                queue.append((i, j))
                visited.add((i, j))
                grid[i][j] = '.'

    # Topological sort to visit the rest
    while len(queue) > 0:
        count += 1
        cur = queue.popleft()
        for i in range(len(DX)):
            nx, ny = DX[i] + cur[0], DY[i] + cur[1]
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == '@' and (nx, ny) not in visited and check(nx, ny) < THRESHOLD:
                visited.add((nx, ny))
                queue.append((nx, ny))
                grid[nx][ny] = '.'

print(count)

                
    