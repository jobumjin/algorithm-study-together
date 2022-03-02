import sys

N = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))
arr.sort()

result = []
last = 0

for i in range(N):
    last += arr[i]
    result.append(last)

print(sum(result))
