import sys

N = int(sys.stdin.readline())
arr = list(map(int, input().split()))
hq = []
d = {}
result = ''

hq = list(set(arr))

hq.sort()

for j in range(len(hq)):
    d[hq[j]] = j

for i in range(N):
    if i == N - 1:
        result += str(d.get(arr[i]))
    else:
        result += str(d.get(arr[i])) + ' '

print(result)
