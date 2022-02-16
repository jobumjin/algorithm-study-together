import sys

N = int(sys.stdin.readline())

d = {}

arr = []
de = [0 for _ in range(N)]

for i in range(N):
    term = int(sys.stdin.readline())
    arr.append(term)
    if not d.get(term, False):
        d[term] = 1
    else:
        d[term] += 1

arr.sort()

darr = []

while d:
    term = d.popitem()
    darr.append([term[1], term[0]])  # sort(key=lambda x: (x[1], x[0])) 에서 key 사용 안돼서 그냥 순서 바꿈

darr.sort()
darr.reverse()

print(int(round(sum(arr)/N, 0)))
print(arr[int(N / 2)])
if len(darr) > 1:
    if darr[0][0] == darr[1][0]:
        darr2 = [darr[0][1]]
        Max = darr[0][0]
        i = 1
        while i < len(darr):
            if darr[i][0] < Max:
                break
            else:
                darr2.append(darr[i][1])
            i += 1
        darr2.sort()
        print(darr2[1])
    else:
        print(darr[0][1])

else:
    print(darr[0][1])
print(arr[-1] - arr[0])

