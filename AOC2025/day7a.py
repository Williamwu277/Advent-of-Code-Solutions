"""
Day 7A
"""

data = []

with open("input.in", "r") as f:
    for line in f:
        data.append(line)
    
indices = set()
N, M = len(data), len(data[0])

for i in range(M):
    if data[0][i] == 'S': indices.add(i)

splits = 0

for i in range(1, N - 1):
    new_indices = set()
    for index in indices:
        if data[i][index] == '^': 
            splits += 1
            new_indices.add(index + 1)
            new_indices.add(index - 1)
        else:
            new_indices.add(index)
    indices = new_indices

print(splits)
