line = input()
lst = [int(q) for q in line]

l, r = 0, len(lst) - 1

ind = 0
res = 0

while l <= r:
    
    if l % 2 == 0:
        for _ in range(lst[l]):
            res += ((l // 2) * ind)
            ind += 1
        l += 1
        
    else:
        if r % 2 == 0:
            while lst[l] > 0 and lst[r] > 0:
                res += ((r // 2) * ind)
                ind += 1
                lst[l] -= 1
                lst[r] -= 1
            
            if lst[l] == 0:
                l += 1
                continue
            
            if lst[r] == 0:
                r -= 2
                continue

print(res)
                
                
                
            
            
            
        
        
        
    