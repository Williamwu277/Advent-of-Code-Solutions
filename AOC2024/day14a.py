# AOC 2024 Day 14


# 500
q = int(input())
n = 101
m = 103
pos = []
spd = []

# parse input
for i in range(q):

    line = input().split()

    p = line[0].split(',')
    v = line[1].split(',')

    pX = int(p[0][2:])
    pY = int(p[1])
    
    vX = int(v[0][2:])
    vY = int(v[1])

    pos.append((pX, pY))
    spd.append((vX, vY))
    
# simulate steps
for step in range(100):
    
    nw = []

    for i in range(len(pos)):

        nwX = (pos[i][0] + spd[i][0]) % n
        nwY = (pos[i][1] + spd[i][1]) % m

        nw.append((nwX, nwY))
    
    pos = nw
    
    
A, B, C, D = 0, 0, 0, 0

# calculate quadrants
for i in range(q):

    if pos[i][0] + 1 <= n//2:

        if pos[i][1] + 1 <= m//2:

            A += 1
        
        elif pos[i][1] + 1 > m//2 + 1:

            B += 1
    
    elif pos[i][0] + 1 > n//2 + 1:

        if pos[i][1] + 1 <= m//2:

            C += 1

        elif pos[i][1] + 1 > m//2 + 1:

            D += 1


print(A * B * C * D)

