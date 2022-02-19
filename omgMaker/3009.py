import sys

c1 = []
c2 = []

for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    if x in c1:
        c1.remove(x)
    else:
        c1.append(x)
    if y in c2:
        c2.remove(y)
    else:
        c2.append(y)

print(c1[0], c2[0])

