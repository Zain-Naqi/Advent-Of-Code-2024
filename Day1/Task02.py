from collections import Counter

leftList = []
rightList = []


for _ in range(1000):
    line = input()
    l = [int(q) for q in line.split()]
    leftList.append(l[0])
    rightList.append(l[1])

rightDic = Counter(rightList)

res = 0
for n in leftList:
    res += (n * rightDic[n])

print(res)
