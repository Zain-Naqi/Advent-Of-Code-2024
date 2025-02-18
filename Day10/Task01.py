from collections import defaultdict

G = []

rows = 44
cols = rows

for i in range(rows):
    line = input()
    G.append([int(q) for q in line])
    
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
def dfs(r, c, visited):
    if G[r][c] == 9:
        visited.append((r, c))
    else:
        for dy, dx in d:
            if ((r + dy) in range(rows) and 
                (c + dx) in range(cols) and
                G[r + dy][c + dx] == 1 + G[r][c]):
                dfs(r + dy, c + dx, visited)

res = 0
        
for i in range(rows):
    for j in range(cols):
        visited = []
        if G[i][j] == 0:
            dfs(i, j, visited)
            res += len(visited)

print(res)
            
            

