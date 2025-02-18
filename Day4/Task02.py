grid = []

for _ in range(140):
    grid.append(input())

res = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'A':
            if (i > 0 and i < len(grid) - 1 and j > 0 and j < len(grid[i]) - 1):
                
                if ((grid[i - 1][j - 1] == 'M' and grid[i + 1][j + 1] == 'S') or 
                    (grid[i - 1][j - 1] == 'S' and grid[i + 1][j + 1] == 'M')):
                    
                    if ((grid[i - 1][j + 1] == 'M' and grid[i + 1][j - 1] == 'S') or 
                        (grid[i - 1][j + 1] == 'S' and grid[i + 1][j - 1] == 'M')):
                        
                        res += 1

print(res)

