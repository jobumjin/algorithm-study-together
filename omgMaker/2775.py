import sys

N = int(sys.stdin.readline())

arr = [[0] * 14 for _ in range(15)]

for i in range(14):
    arr[0][i] = i+1

result = []

for c in range(N):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    for i in range(1, k+1):
        for j in range(n):
            if arr[i][j] == 0:
                total = 0
                for l in range(j+1):
                    total += arr[i - 1][l]
                arr[i][j] = total

    result.append(arr[i][j])

for i in range(N):
    print(result[i])
