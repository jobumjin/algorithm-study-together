import sys

N, L = map(int, sys.stdin.readline().split())

arr = []
for i in range(N):
    arr.append(i)

for _ in range(L):
    term1, term2 = map(int, sys.stdin.readline().split())
    target = arr[term2 - 1]
    if target != arr[term1 - 1]:
        while arr.count(target) > 0:
            arr[arr.index(target)] = arr[term1 - 1]

arr = set(arr)
print(len(arr))

