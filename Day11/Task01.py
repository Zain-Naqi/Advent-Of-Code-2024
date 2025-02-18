line = input()
l = [int(q) for q in line.split()]

stones = len(l)
for _ in range(25):
    temp = []
    for n in l:
        if n == 0:
            temp.append(1)
        elif len(str(n)) % 2 == 0:
            temp.append(int(str(n)[:len(str(n))//2]))
            s = str(n)[(len(str(n))//2):]
            temp.append(int(s))
        else:
            temp.append(n * 2024)
    l = temp

print(len(temp))
    