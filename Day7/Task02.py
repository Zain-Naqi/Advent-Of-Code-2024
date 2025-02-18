def validOperators(target, nums):
    
    def isValid(currVal, i):
        if currVal == target and i == len(nums):
            return True
        if i == len(nums):
            return False
        return (isValid(currVal * nums[i], i + 1) or 
                isValid(currVal + nums[i], i + 1) or
                isValid(int(str(currVal) + str(nums[i])), i + 1))
    
    return isValid(nums[0], 1)
        

Tests = {}

for _ in range(850):
    line = input()
    temp = line.split(':')
    Tests[int(temp[0])] = [int(q) for q in temp[1].split()]

res = 0
for t in Tests:
    if validOperators(t, Tests[t]):
        res += t

print(res)
        

