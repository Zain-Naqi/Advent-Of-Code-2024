G = []

rows = 50
for _ in range(rows):
    line = input()
    G.append(list(line))

cols = len(G[0])

path = ""
for _ in range(20):
    path += input()

currX, currY = 0, 0
for i in range(rows):
    for j in range(cols):
        if G[i][j] == '@':
            currX, currY = j, i

def move(dx, dy, currX, currY):
    if G[currY + dy][currX + dx] != '#':
        if G[currY + dy][currX + dx] != 'O':
            G[currY + dy][currX  + dx] = '@'
            G[currY][currX] = '.'
            return True
        else:
            tempX, tempY = currX + dx, currY + dy
            while G[tempY][tempX] == 'O':
                tempX += dx
                tempY += dy
            if G[tempY][tempX] == '#':
                return False
            else:
                G[tempY][tempX] = 'O'
                G[currY + dy][currX + dx] = '@'
                G[currY][currX] = '.'
                return True
    else:
        return False
                    
for d in path:
    if d == '^':
        if move(0, -1, currX, currY):
            currY += -1
            currX += 0
    elif d == '>':
        if move(1, 0, currX, currY):
            currY += 0
            currX += 1
    elif d == 'v':
        if move(0, 1, currX, currY):
            currY += 1
            currX += 0
    else:
        if move(-1, 0, currX, currY):
            currY +=0
            currX += -1
        
res = 0
for i in range(rows):
    for j in range(cols):
        if G[i][j] == 'O':
            res += (100 * i + j)

print(res)
    
