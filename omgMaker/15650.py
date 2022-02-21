import sys
from itertools import combinations  # 순열

N, M = map(int, sys.stdin.readline().split())

v = []

for i in range(1, N+1):
    v.append(i)

tu = combinations(v, M)
arr = list(tu)

for i in arr:
    result = ''
    for j in i:
        result += str(j) + ' '
    print(result)