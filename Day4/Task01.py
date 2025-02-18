grid = []

for _ in range(140):
    grid.append(input())

res = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'X':
           
            if j + 3 < len(grid[i]) and grid[i][j:j + 4] == "XMAS":
                res += 1
            
            if j - 3 >= 0 and grid[i][j - 3:j + 1][::-1] == "XMAS":
                res += 1
            
            if i + 3 < len(grid) and grid[i + 1][j] + grid[i + 2][j] + grid[i + 3][j] == "MAS":
                res += 1
        
            if i - 3 >= 0 and grid[i - 3][j] + grid[i - 2][j] + grid[i - 1][j] == "SAM":
                res += 1
            
            if (i + 3 < len(grid) and j + 3 < len(grid[i]) and 
               grid[i + 1][j + 1] + grid[i + 2][j + 2] + grid[i + 3][j + 3] == "MAS"):
                res += 1
            
            if (i - 3 >= 0 and j - 3 >= 0 and 
               grid[i - 1][j - 1] + grid[i - 2][j - 2] + grid[i - 3][j - 3] == "MAS"):
                res += 1
            
            if (i + 3 < len(grid) and j - 3 >= 0 and 
               grid[i + 1][j - 1] + grid[i + 2][j - 2] + grid[i + 3][j - 3] == "MAS"):
                res += 1
            
            if (i - 3 >= 0 and j + 3 < len(grid[i]) and 
               grid[i - 1][j + 1] + grid[i - 2][j + 2] + grid[i - 3][j + 3] == "MAS"):
                res += 1

print(res)

