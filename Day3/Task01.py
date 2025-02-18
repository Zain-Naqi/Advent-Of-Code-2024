import re

text = ""
for _ in range(6):
    text += input()

muls = re.findall(r"mul\((\d+),(\d+)\)", text)

res = 0

for mul in muls:
    res += (int(mul[0]) * int(mul[1]))

print(res)
