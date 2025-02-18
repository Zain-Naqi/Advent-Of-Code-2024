G = []

rows = 140
cols = rows

for i in range(rows):
    line = input()
    G.append(list(line))
    
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def addInSet(r, c, top, bottom, left, right):
    
    if r - 1 < 0 or G[r - 1][c] != G[r][c]:
        top.add((r, c))
    
    if r + 1 >= rows or G[r + 1][c] != G[r][c]:
        bottom.add((r, c))
    
    if c - 1 < 0 or G[r][c - 1] != G[r][c]:
        left.add((r, c))
    
    if c + 1 >= cols or G[r][c + 1] != G[r][c]:
        right.add((r, c))
        
        
def calParameter(top, bottom, left, right):
    p = 0
    
    top = sorted(list(top), key = lambda x: (x[0], x[1]))
    if len(top) > 0:
        p += 1
        for i in range(1, len(top)):
            if top[i][0] != top[i - 1][0] or top[i][1] != top[i - 1][1] + 1:
                p += 1
    
    bottom = sorted(list(bottom), key = lambda x: (x[0], x[1]))
    if len(bottom) > 0:
        p += 1
        for i in range(1, len(bottom)):
            if bottom[i][0] != bottom[i - 1][0] or bottom[i][1] != bottom[i - 1][1] + 1:
                p += 1
                
    left = sorted(list(left), key = lambda x: (x[1], x[0]))
    if len(left) > 0:
        p += 1
        for i in range(1, len(left)):
            if left[i][0] != left[i - 1][0] + 1 or left[i][1] != left[i - 1][1]:
                p += 1
    
    right = sorted(list(right), key = lambda x: (x[1], x[0]))
    if len(right) > 0:
        p += 1
        for i in range(1, len(right)):
            if right[i][0] != right[i - 1][0] + 1 or right[i][1] != right[i - 1][1]:
                p += 1
    
    return p
            
visited = set()


def bfs(r, c, top, bottom, left, right):
    
    area = 0
    perimeter = 0
    
    queue = [(r, c)]
    visited.add((r, c))
    
    while queue:
        i, j = queue.pop(0)
        area += 1
        addInSet(i, j, top, bottom, left, right)
        
        for dy, dx in d:
            if ((i + dy, j + dx) not in visited and
                i + dy in range(rows) and 
                j + dx in range(cols) and
                G[i + dy][j + dx] == G[r][c]):
                visited.add((i + dy, j + dx))
                queue.append((i + dy, j + dx))
    
    perimeter = calParameter(top, bottom, left, right)
    
    return area * perimeter


res = 0
                
for i in range(rows):
    for j in range(cols):
        if (i, j) not in visited:
            top, bottom, left, right = set(), set(), set(), set()
            res += bfs(i, j, top, bottom, left, right)

print(res)
        