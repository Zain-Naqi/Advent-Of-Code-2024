leftList = []
rightList = []


for _ in range(1000):
    line = input()
    l = [int(q) for q in line.split()]
    leftList.append(l[0])
    rightList.append(l[1])
    

leftList.sort()
rightList.sort()

res = 0
for l, r in zip(leftList, rightList):
    res += abs(l - r)

print(res)
    

    
    