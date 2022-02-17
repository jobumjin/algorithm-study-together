import sys

N = int(sys.stdin.readline())

i = 1
result = 0
while True:
    term = result
    result += i

    if result >= N:
        if i % 2 == 1:
            num = result - N
            s = str(num + 1) + '/' + str(i - num) # i - 1 - num + 1
            print(s)
        else:
            num = result - N
            s = str(i - num) + '/' + str(num + 1)
            print(s)

        break

    i += 1

