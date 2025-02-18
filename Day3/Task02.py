import re

text = ""
for _ in range(6):
    text += input()

muls = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", text)

flag = True
res = 0

for mul in muls:
    if mul == "don't()":
        flag = False
        continue
    if mul == "do()":
        flag = True
        continue
    
    if flag:
        temp = re.findall(r'\d+', mul)
        res += (int(temp[0]) * int(temp[1]))
    
print(res)
