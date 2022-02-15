import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, input().split()))

mx = 0

for i in combinations(arr, 3):
    if sum(i) <= M and M - mx > M - sum(i):
        mx = sum(i)

print(mx)
