from collections import defaultdict

G = []
for _ in range(50):
    line = input()
    G.append(list(line))

A = defaultdict(list)

for i in range(len(G)):
    for j in range(len(G[0])):
        if G[i][j] != '.':
            A[G[i][j]].append((i, j))

D = set()

for antenna in A:
    for i in range(len(A[antenna])):
        for j in range(i + 1, len(A[antenna])):
            
            t1, t2 = A[antenna][i], A[antenna][j]
            
            D.add(t1)
            D.add(t2)
            
            d = (t2[0] - t1[0], t2[1] - t1[1]) 
            
            p = (t2[0] + d[0], t2[1] + d[1])
            while 0 <= p[0] < len(G) and 0 <= p[1] < len(G[0]):
                D.add(p)
                p = (p[0] + d[0], p[1] + d[1])
            
            dlt = (d[0] * -1, d[1] * -1)
            p = (t1[0] + dlt[0], t1[1] + dlt[1])
            while 0 <= p[0] < len(G) and 0 <= p[1] < len(G[0]):
                D.add(p)
                p = (p[0] + dlt[0], p[1] + dlt[1])

print(len(D))
