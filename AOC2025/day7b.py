"""
Day 7B
Initially thought it was DP
Kind of still is, but we only need a 1D array
"""

data = []

with open("input.in", "r") as f:
    for line in f:
        data.append(line)
    
N, M = len(data), len(data[0])
rows = [1 for _ in range(M)]
S_row = -1

for i in range(M):
    if data[0][i] == 'S': S_row = i

for i in range(N - 1, -1, -1):
    new_rows = [0 for _ in range(M)]
    for j in range(M):
        if data[i][j] == '^': new_rows[j] = rows[j - 1] + rows[j + 1]
        else: new_rows[j] = rows[j]
    rows = new_rows

print(rows[S_row])
