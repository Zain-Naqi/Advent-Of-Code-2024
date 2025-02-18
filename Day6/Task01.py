G = []

rows = 130

for _ in range(rows):
    G.append(input())

cols = len(G[0])

currY, currX = 0, 0
for i in range(rows):
    for j in range(cols):
        if G[i][j] == '^':
            currY, currX = i, j

visited = set()
currDir = "UP"
visited.add((currX, currY)) 

while (0 <= currY < rows) and (0 <= currX < cols):
    
    if currDir == "UP":
        while currY >= 0 and G[currY][currX] != '#':
            visited.add((currX, currY))
            currY -= 1
        if currY >= 0 and G[currY][currX] == '#':
            currY += 1
            currDir = 'RIGHT'

    elif currDir == "RIGHT":
        while currX < cols and G[currY][currX] != '#':
            visited.add((currX, currY))
            currX += 1
        if currX < cols and G[currY][currX] == '#':
            currX -= 1
            currDir = 'DOWN'

    elif currDir == "DOWN":
        while currY < rows and G[currY][currX] != '#':
            visited.add((currX, currY))
            currY += 1
        if currY < rows and G[currY][currX] == '#':
            currY -= 1
            currDir = 'LEFT'

    elif currDir == "LEFT":
        while currX >= 0 and G[currY][currX] != '#':
            visited.add((currX, currY))
            currX -= 1
        if currX >= 0 and G[currY][currX] == '#':
            currX += 1
            currDir = 'UP'
            

print(len(visited))
