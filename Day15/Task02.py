tempG = []

rows = 50
for _ in range(rows):
    line = input()
    tempG.append(list(line))

cols = len(tempG[0])

path = ""
for _ in range(20):
    path += input()

G = []
for i in range(rows):
    temp = []
    for j in range(cols):
        if tempG[i][j] == '@':
            temp.append('@')
            temp.append('.')
        elif tempG[i][j] == 'O':
            temp.append('[')
            temp.append(']')
        else:
            temp.append(tempG[i][j])
            temp.append(tempG[i][j])
    G.append(temp)
    

cols = cols * 2

currX, currY = 0, 0
for i in range(rows):
    for j in range(cols):
        if G[i][j] == '@':
            currX, currY = j, i

def move(dx, dy, currX, currY, vertical):
    if G[currY + dy][currX + dx] != '#':
        if G[currY + dy][currX + dx] not in '[]':
            G[currY + dy][currX + dx] = '@'
            G[currY][currX] = '.'
            return True
        else:
            if not vertical:
                tempX, tempY = currX + dx, currY + dy
                while G[tempY][tempX] in '[]':
                    tempX += dx
                    tempY += dy
                if G[tempY][tempX] == '#':
                    return False
                else:
                    G[tempY][tempX] = G[tempY - dy][tempX - dx]
                    tempY -= dy
                    tempX -= dx

                    while G[tempY][tempX] in "[]":
                        if G[tempY][tempX] == '[':
                            G[tempY][tempX] = ']'
                        else:
                            G[tempY][tempX] = '['
                        tempY -= dy
                        tempX -= dx
                    
                    G[currY + dy][currX + dx] = '@'
                    G[currY][currX] = '.'
                    return True
            else:
                tempX, tempY = currX + dx, currY + dy
                stack = [(tempX, tempY)]
                visited = set()
                visited.add((tempX, tempY))
                while stack:
                    x, y = stack.pop()
                    if G[y + dy][x] == '#':
                        return False
                    if G[y][x] == '[' and (x + 1, y) not in visited:
                        stack.append((x + 1, y))
                        visited.add((x + 1, y))
                    if G[y][x] == ']' and (x - 1, y) not in visited:
                        stack.append((x - 1, y))
                        visited.add((x - 1, y))
                    if G[y + dy][x] in '[]' and (x, y + dy) not in visited:
                        stack.append((x, y + dy))
                        visited.add((x, y + dy))
                        
                visited = sorted(visited, key=lambda t: (t[1], t[0]))
                for x, y in visited:
                    G[y + dy][x] = G[y][x]
                    G[y][x] = '.'
                if G[tempY][tempX] == '[' and G[tempY][tempX + 1] == ']':
                    G[tempY][tempX + 1] = '.'
                elif G[tempY][tempX] == ']' and G[tempY][tempX - 1] == '[':
                    G[tempY][tempX - 1] = '.'
                G[tempY][tempX] = '@'
                G[currY][currX] = '.'
                return True         
    else:
        return False

            
for d in path:
    if d == '^':
        if move(0, -1, currX, currY, True):
            currY += -1
            currX += 0
    elif d == '>':
        if move(1, 0, currX, currY, False):
            currY += 0
            currX += 1
    elif d == 'v':
        if move(0, 1, currX, currY, True):
            currY += 1
            currX += 0
    else:
        if move(-1, 0, currX, currY, False):
            currY +=0
            currX += -1
    
res = 0
for i in range(rows):
    for j in range(cols):
        if G[i][j] == '[':
            res += (100 * i + j)
            
print(G)
print(res)
