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
    
# check first 10000 steps for the criteria for a tree
for step in range(10000):
    
    # update positions for one step
    nw = []

    for i in range(len(pos)):

        nwX = (pos[i][0] + spd[i][0]) % n
        nwY = (pos[i][1] + spd[i][1]) % m

        nw.append((nwX, nwY))
    
    pos = nw

    # create a grid
    arr = []

    for k in range(n):

        arr.append([])
        
        for j in range(m):
            
            arr[k].append(0)

    for k in range(q):

        arr[pos[k][0]][pos[k][1]] += 1
    
    # check for the tree shape
    # if the image has both 30+ filled in rows and cols its a hit
    vert = False
    hori = False
    
    for k in range(n):

        row_sz = 0

        for j in range(m):

            if arr[k][j] > 0:

                row_sz += 1
        
        if row_sz > 30:
            
            hori = True
    
    for j in range(m):

        col_sz = 0

        for k in range(n):

            if arr[k][j] > 0:

                col_sz += 1
        
        if col_sz > 30:

            vert = True

    # check progress
    if step % 1000 == 0:

        print(step)

    # print out any hits
    if vert and hori:

        print("GRID", step)

        for k in range(n):

            for j in range(m):

                if arr[k][j] > 0:

                    print('*', end='')
                    
                else:

                    print(' ', end='')
            
            print()
                
        print()
