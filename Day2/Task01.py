res = 0

for _ in range(1000):
    line = input()
    l = [int(q) for q in line.split()]
    
    flag = True
    if l == sorted(l) or l == sorted(l)[::-1]:
        for i in range(1, len(l)):
            if abs(l[i] - l[i - 1]) < 1 or abs(l[i] - l[i - 1]) > 3:
                flag = False
                break 
        if flag:
            res += 1
    
print(res)
    