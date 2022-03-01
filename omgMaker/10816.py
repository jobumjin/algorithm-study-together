import sys

N = int(sys.stdin.readline())

d = {}

arr = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    term = arr[i]
    value = d.get(term)
    if value is None:
        d[term] = 1
    else:
        d[term] = value + 1

M = int(sys.stdin.readline())

arr2 = list(map(int, sys.stdin.readline().split()))

result = ''
for i in range(M):
    term = arr2[i]
    value = d.get(term)
    if value is None:
        result += str(0) + ' '
    else:
        result += str(value) + ' '

print(result)