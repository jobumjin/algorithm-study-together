import sys

N = int(sys.stdin.readline())

arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline()))

cache = [1, 2, 4]

for i in range(3, max(arr)):
    cache.append(cache[i - 3] + cache[i - 2] + cache[i - 1])

for i in range(N):
    print(cache[arr[i] - 1])