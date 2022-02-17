import sys

N = int(sys.stdin.readline())

i = 0
result = 1
while True:
    result += i * 6
    i += 1
    if N <= result:
        break

print(i)