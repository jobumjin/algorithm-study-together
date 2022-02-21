import sys
from itertools import combinations  # 순열

N = int(sys.stdin.readline())

board = []
for i in range(N):
    board.append(list(map(int, input().split())))

v = []

for i in range(0, N):
    v.append(i)

tu = combinations(v, int(N/2))
arr = list(tu)
result_arr = []
count = 0
for i in arr:
    if count == int(len(arr)/2):
        break
    else:
        count += 1

    term = []
    for j in i:
        term.append(j)

    term2 = v.copy()
    for j in range(len(term)):
        term2.remove(term[j])

    total1 = 0

    for j in term:
        for k in term:
            if i != k:
                total1 += board[j][k]

    total2 = 0

    for j in term2:
        for k in term2:
            if i != k:
                total2 += board[j][k]

    result_arr.append(abs(total1 - total2))

print(min(result_arr))