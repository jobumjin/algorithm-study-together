import sys

N, M = map(int, sys.stdin.readline().split())

arr = []
for i in range(N):
    if i == 0:
        arr.append(N)
    else:
        arr.append(i)

result = []

term = 0
last = -1
while True:
    for i in range(M):
        term += 1
        if term == len(arr):
            term = 0

    item = arr.pop(term)
    result.append(item)
    term -= 1

    if len(arr) == 0:
        break

result_sum = '<'
for i in range(N):
    if i != N - 1:
        result_sum += str(result[i]) + ', '
    else:
        result_sum += str(result[i]) + '>'

print(result_sum)