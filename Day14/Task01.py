import re

rows = 103
cols = 101
t = 100

finalPos = []

for i in range(500):
    line = input()
    numbers = re.findall(r"-?\d+", line)
    numbers = [int(num) for num in numbers]
    
    x, y = numbers[0], numbers[1]
    dx, dy = numbers[2], numbers[3]
    
    finalPos.append(((x + (t * dx)) % cols, (y + (t * dy)) % rows))

def quadrant(x, y):
    if x == cols // 2 or y == rows // 2:
        return 0
    
    elif x < cols // 2 and y < rows // 2:
        return 1
    
    elif x > cols // 2 and y < rows // 2:
        return 2
    
    elif x < cols // 2 and y > rows // 2:
        return 3
    
    elif x > cols // 2 and y > rows // 2:
        return 4

q = {1:0, 2:0, 3:0, 4:0}
for x, y in finalPos:
    quad = quadrant(x, y)
    if quad != 0:
        q[quad] += 1
    
print(q[1] * q[2] * q[3] * q[4])
    
        

    
    
    
    