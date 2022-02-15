#  부르트 포스, 자릿수

import sys

N = int(sys.stdin.readline())

result = 0

for i in range(1, N):
    strI = str(i)
    size = len(strI)
    num = i
    for j in range(size):
        num += int(strI[j])

    if num == N:
        result = i
        break

print(result)
