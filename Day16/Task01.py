import heapq

G = []

input()

rows = 139

for _ in range(rows):
    G.append(list(input()[:-1])[1:])
 
cols = len(G[0])

# East, South, West, North
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] 
     
minHeap = [(0, 0, rows - 1, 0)]
visited = set()
res = float('inf')

while minHeap:
    currScore, x, y, currDir = heapq.heappop(minHeap)
    
    if (x, y) == (cols - 1, 0):
        res = min(res, currScore)
    
    if (x, y, currDir) in visited:
        continue
    
    visited.add((x, y, currDir))
    
    # Travel in same direction:
    dy, dx = y + directions[currDir][1], x + directions[currDir][0]
    if 0 <= dx < cols and 0 <= dy < rows and G[dy][dx] != '#': 
        heapq.heappush(minHeap, (currScore + 1, dx, dy, currDir))
    
    # Turn right:
    newDir = (currDir + 1) % 4
    dx, dy = x + directions[newDir][0], y + directions[newDir][1]
    if 0 <= dx < cols and 0 <= dy < rows and G[dy][dx] != '#':
        heapq.heappush(minHeap, (currScore + 1001, dx, dy, newDir))
    
    # Turn left:
    newDir = (currDir - 1) % 4
    dx, dy = x + directions[newDir][0], y + directions[newDir][1]
    if 0 <= dx < cols and 0 <= dy < rows and G[dy][dx] != '#':
        heapq.heappush(minHeap, (currScore + 1001, dx, dy, newDir))
    
print(res)
