line = input()
bp = [int(q) for q in line]
lst = [int(q) for q in line]

l, r = 0, len(lst) - 1

ind = 0
res = 0
visited = set()

while l <= r:
    
    if l in visited and l % 2 == 0:
        ind += bp[l]
        l += 1
        continue 
            
    if l % 2 == 0 and l not in visited:
        for _ in range(lst[l]):
            res += ((l // 2) * ind)
            ind += 1
        visited.add(l)
        l += 1
        
    else:
        if r % 2 == 0:
            
            temp = r
            while (lst[temp] > lst[l] and l < temp) or temp in visited:
                temp -= 2
            
            if temp > l and temp not in visited:
                
                visited.add(temp)
                
                while lst[temp] > 0:
                    res += ((temp // 2) * ind)
                    ind += 1
                    lst[l] -= 1
                    lst[temp] -= 1
            
                if lst[l] == 0:
                    l += 1
                
                if temp == r:
                    r -= 2
            
            else:
                while lst[l] > 0 and l not in visited:
                    lst[l] -= 1
                    ind += 1
                l += 1
                    
print(res)
