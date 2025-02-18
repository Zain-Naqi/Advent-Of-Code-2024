from collections import defaultdict

G = defaultdict(set)

n, m = 1176, 192
# n, m = 21, 6


for _ in range(n):
    line = input()
    v1, v2 = int(line[0:2]), int(line[3:5])
    G[v1].add(v2)
    
res = 0
d = []

for _ in range(m):
    line = input()
    l = [int(q) for q in line.split(',')]
    
    flag = True
    
    for k in range(len(l)):
        for i in range(len(l) - 1, -1, -1):
            

            for j  in range(i + 1, len(l)):
                if l[j] not in G[l[i]]:
                    flag = False
                    l[i], l[j] = l[j], l[i]
                
    if not flag:
        res += l[len(l)//2]

print(res)
        
        