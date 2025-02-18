import heapq

G = []

input()

rows = 139

for _ in range(rows):
    G.append(list(input()[:-1])[1:])
 
cols = len(G[0])

# East, South, West, North
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] 
     
minHeap = [(0, 0, rows - 1, 0, [(0, rows - 1)])]
visited = set()
res = float('inf')

shortestPaths = []

while minHeap:
    currScore, x, y, currDir, currPath = heapq.heappop(minHeap)
    
    if (x, y) == (cols - 1, 0):
        if currScore < res:
            res = currScore
            shortestPaths = [currPath]
        elif currScore == res:
            shortestPaths.append(currPath)
    
    visited.add((x, y, currDir))
        
    # Travel in same direction:
    dy, dx = y + directions[currDir][1], x + directions[currDir][0]
    if 0 <= dx < cols and 0 <= dy < rows and G[dy][dx] != '#' and (dx, dy, currDir) not in visited: 
        heapq.heappush(minHeap, (currScore + 1, dx, dy, currDir, currPath + [(dx, dy)]))
    
    # Turn right:
    newDir = (currDir + 1) % 4
    dx, dy = x + directions[newDir][0], y + directions[newDir][1]
    if 0 <= dx < cols and 0 <= dy < rows and G[dy][dx] != '#' and (dx, dy, newDir) not in visited:
        heapq.heappush(minHeap, (currScore + 1001, dx, dy, newDir, currPath + [(dx, dy)]))
    
    # Turn left:
    newDir = (currDir - 1) % 4
    dx, dy = x + directions[newDir][0], y + directions[newDir][1]
    if 0 <= dx < cols and 0 <= dy < rows and G[dy][dx] != '#' and (dx, dy, newDir) not in visited:
        heapq.heappush(minHeap, (currScore + 1001, dx, dy, newDir, currPath + [(dx, dy)]))
            
uniqueCells = set(node for path in shortestPaths for node in path)
print(len(uniqueCells))
