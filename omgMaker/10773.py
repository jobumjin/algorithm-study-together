import sys

N = int(sys.stdin.readline())
arr = []
s = []

for i in range(N):
    arr.append(int(sys.stdin.readline()))

for i in range(N):
    if arr[i] == 0 and len(s) != 0:
        s.pop()
    else:
        s.append(arr[i])

print(sum(s))
