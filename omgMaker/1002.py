import sys

N = int(input())

for i in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = ((x2-x1) ** 2 + (y2-y1) ** 2) ** (1/2)

    if r1 > r2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        r1, r2 = r2, r1

    if r2 + r1 > d > r2 - r1:
        print(2)
    elif r2 + r1 == d or (r2 - r1 == d and r1 != r2):
        print(1)
    elif r1 + r2 < d or d < r2 - r1 or (x1 == x2 and y1 == y2 and r1 != r2):
        print(0)
    elif x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)