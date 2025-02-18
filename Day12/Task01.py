G = []

rows = 140
cols = rows

for i in range(rows):
    line = input()
    G.append(list(line))
    
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def numSides(r, c):
    count = 0
    for dy, dx in d:
        if r + dy >= rows or c + dx >= cols or r + dy < 0 or c + dx < 0:
            count += 1
        elif G[r + dy][c + dx] != G[r][c]:
            count += 1

    return count
    
visited = set()

def bfs(r, c):
    
    area = 0
    perimeter = 0
    
    queue = [(r, c)]
    visited.add((r, c))
    
    while queue:
        i, j = queue.pop(0)
        area += 1
        perimeter += numSides(i, j)
        
        for dy, dx in d:
            if ((i +dy, j + dx) not in visited and
                i + dy in range(rows) and 
                j + dx in range(cols) and
                G[i + dy][j + dx] == G[r][c]):
                visited.add((i + dy, j + dx))
                queue.append((i + dy, j + dx))
    
    return area * perimeter

res = 0
                
for i in range(rows):
    for j in range(cols):
        if (i, j) not in visited:
            res += bfs(i, j)

print(res)
        