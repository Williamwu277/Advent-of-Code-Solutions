# AOC 2024 Day 15


# 50 by 50
# 20 lines

n = 50
m = 50
q = 20
arr = []
indX, indY = -1, -1

for i in range(n):

    arr.append([])
    line = input()
    
    for j in range(m):

        arr[i].append(line[j])

        if line[j] == '@':

            indX = i
            indY = j

input()
moves = ""

for i in range(q):

    moves += input().rstrip()

for s in range(len(moves)):

    flag = -1

    if moves[s] == '^':

        for i in range(indX-1, -1, -1):

            if arr[i][indY] == '.':

                flag = i
                break

            elif arr[i][indY] == '#':

                break
        
        if flag == indX-1:

            arr[indX-1][indY] = '@'
            arr[indX][indY] = '.'
            indX -= 1

        elif flag >= 0:

            arr[flag][indY] = 'O'
            arr[indX][indY] = '.'
            arr[indX-1][indY] = '@'
            indX -= 1

    elif moves[s] == 'v':

        for i in range(indX+1, n):

            if arr[i][indY] == '.':

                flag = i
                break
            
            elif arr[i][indY] == '#':

                break
        
        if flag == indX+1:

            arr[indX+1][indY] = '@'
            arr[indX][indY] = '.'
            indX += 1

        elif flag >= 0:

            arr[flag][indY] = 'O'
            arr[indX][indY] = '.'
            arr[indX+1][indY] = '@'
            indX += 1
    
    elif moves[s] == '<':

        for i in range(indY-1, -1, -1):

            if arr[indX][i] == '.':

                flag = i
                break
            
            elif arr[indX][i] == '#':

                break
        
        if flag == indY-1:

            arr[indX][indY-1] = '@'
            arr[indX][indY] = '.'
            indY -= 1

        elif flag >= 0:

            arr[indX][flag] = 'O'
            arr[indX][indY] = '.'
            arr[indX][indY-1] = '@'
            indY -= 1
    
    else:

        for i in range(indY+1, m):

            if arr[indX][i] == '.':

                flag = i
                break
                
            elif arr[indX][i] == '#':

                break
        
        if flag == indY+1:

            arr[indX][indY+1] = '@'
            arr[indX][indY] = '.'
            indY += 1

        elif flag >= 0:

            arr[indX][flag] = 'O'
            arr[indX][indY] = '.'
            arr[indX][indY+1] = '@'
            indY += 1
    
score = 0

for i in range(n):
            
    for j in range(m):

        if arr[i][j] == 'O':

            score += i * 100 + j

print(score)

