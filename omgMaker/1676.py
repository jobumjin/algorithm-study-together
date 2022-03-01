import sys

N = int(sys.stdin.readline())

result = 1

if N == 0:
    print(0)
else:
    for i in range(1, N+1):
        result *= i

    str_result = str(result)

    count = 0

    for i in range(len(str_result) - 1, -1, -1):
        if str_result[i] == '0':
            count += 1
        else:
            break

    print(count)
