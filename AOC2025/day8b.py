"""
Day 8B
Similar to the first part
"""

id_count = 1
points = dict()

with open("input.in", "r") as f:
    for line in f:
        points[id_count] = tuple(map(int, line.split(',')))
        id_count += 1
    
connections = []

for i in range(1, id_count):
    for j in range(i + 1, id_count):
        distance = (
            (points[i][0] - points[j][0]) ** 2 +
            (points[i][1] - points[j][1]) ** 2 +
            (points[i][2] - points[j][2]) ** 2
        )
        connections.append((distance, i, j))

connections.sort()
leader, sz = [i for i in range(id_count)], [1 for _ in range(id_count)]

def find(cur):
    while cur != leader[cur]:
        cur = leader[cur]
    return cur

def union(first, second):
    first = find(first)
    second = find(second)
    if first == second: return False
    if sz[second] > sz[first]: first, second = second, first
    sz[first] += sz[second]
    leader[second] = first
    return True

connection_score = 0
for connection in connections:
    _, first, second = connection
    if sz[find(first)] == id_count - 1: break
    union(first, second)
    connection_score = points[first][0] * points[second][0]

print(connection_score)
