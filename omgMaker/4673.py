m = 10000

result = [False for _ in range(m)]

for i in range(m):
    strI = str(i)
    size = len(strI)
    num = 0
    for j in range(size):
        num += int(strI[j])
    target = i + num

    if target >= m:
        continue
    else:
        result[target - 1] = True


for i in range(m):
    if not result[i]:
        print(i+1)
