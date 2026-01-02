"""
Day 8A
This problem kind of follows the kruskals algorithm flow. Create edges between all nodes
and then sort them. Then add the number of edges specified
"""

MAX_CONNECTIONS = 1000

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

connections_made = 0
for connection in connections:
    _, first, second = connection
    if connections_made >= MAX_CONNECTIONS: break
    union(first, second)
    connections_made += 1

group_sizes = []
for i in range(1, id_count):
    if leader[i] == i: group_sizes.append(sz[i])

group_sizes.sort(reverse=True)
print(group_sizes[0] * group_sizes[1] * group_sizes[2])
