import sys

N = int(sys.stdin.readline())

arr = []

for i in range(N):
    H, W, C = map(int, sys.stdin.readline().split())

    C -= 1

    result = ''

    if int(C / H) + 1 >= 10:
        result += str(C % H + 1) + str(int(C / H) + 1)
    else:
        result += str(C % H + 1) + '0' + str(int(C / H) + 1)

    arr.append(result)

for i in range(N):
    print(arr[i])

