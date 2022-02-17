import sys

N = int(sys.stdin.readline())

arr = [[' '] * N for _ in range(N)]

arr[0][0] = '*'

start = 3

while start <= N:
    term = int(start / 3)
    for i in range(3):
        for j in range(3):
            if i == 0 and j == 0:
                continue
            elif i == 1 and j == 1:
                continue
            else:
                for k in range(term):
                    for l in range(term):
                        arr[(i * term) + k][(j * term) + l] = arr[k][l]

    start *= 3

for i in range(N):
    result = ''
    for j in range(N):
        result += arr[i][j]
    print(result)
