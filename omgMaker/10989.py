import sys

N = int(sys.stdin.readline())

arr = [0 for _ in range(10000)]

mx = -1

for i in range(N):
    term = int(sys.stdin.readline())
    arr[term-1] += 1
    if mx < term:
        mx = term

for j in range(mx):
    if arr[j] != 0:
        for k in range(arr[j]):
            print(j+1)
