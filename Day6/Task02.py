G = []

rows = 130
for _ in range(rows):
    line = input()
    G.append(list(line))

cols = len(G[0])
    
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
sr, sc, sd = None, None, None
for r in range(rows):
    for c in range(cols):
        if G[r][c] in "^>v<":
            sr, sc = r, c
            sd = "^>v<".index(G[r][c])  
            break

def eval(obstacle_row, obstacle_col):
    gr, gc, gd = sr, sc, sd
    visited = set()
    visited.add(f"{gr},{gc},{gd}")

    while True:
        dr, dc = dirs[gd]
        next_row = gr + dr
        next_col = gc + dc

        if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
            return False  

        next_cell = (
            "#"
            if (next_row == obstacle_row and next_col == obstacle_col)
            else G[next_row][next_col]
        )
        if next_cell == "#":
            gd = (gd + 1) % 4
        else:
            gr = next_row
            gc = next_col

        state = f"{gr},{gc},{gd}"
        if state in visited:
            return True  
        visited.add(state)

res = 0

for r in range(rows):
    for c in range(cols):
        if G[r][c] == "#" or (r == sr and c == sc):
            continue

        if eval(r, c):
            res += 1

print(res)
