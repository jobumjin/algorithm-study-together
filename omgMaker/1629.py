import sys

A, B, C = map(int, sys.stdin.readline().split())

cache = []


arr = []
while B > 0:
    arr.append(B % 2)
    B //= 2


for i in range(len(arr)):
    if i == 0:
        cache.append(A % C)
    else:
        cache.append((cache[i - 1] ** 2) % C)


result_term = 1
for i in range(len(arr)):
    if arr[i] == 1:
        result_term *= cache[i]
print(result_term % C)