line = input()
l = [int(q) for q in line.split()]

dp = {}

def solve(n, i):
    if i == 0:
        return 1
    
    if (n, i) in dp:
        return dp[(n, i)]
    
    if n == 0:
        dp[(n, i)] = solve(1, i - 1)
        return dp[(n, i)]
    
    if len(str(n)) % 2 == 0:
        left = int(str(n)[:len(str(n))//2])
        right = int(str(n)[(len(str(n))//2):])
        dp[(n, i)] = solve(left, i - 1) + solve(right, i - 1)
        return dp[(n, i)]
    
    else:
        dp[(n, i)] = solve(n * 2024, i - 1)
        return dp[(n, i)]
    

res = 0
for i in range(len(l)):
    res += solve(l[i], 75)

print(res)
