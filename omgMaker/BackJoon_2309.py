import sys
from itertools import combinations

putNum = sys.stdin.readline

v = []

for _ in range(9):
    v.append(int(putNum()))

v.sort()

for i in combinations(v, 7):
    if sum(i) == 100:
        for j in range(len(i)):
            print(i[j])
        break
