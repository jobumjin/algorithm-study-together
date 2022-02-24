import sys

T = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

if len(arr) == 1:
    print(arr[0] ** 2)
else:
    print(arr[0] * arr[-1])