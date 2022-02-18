import sys

M = int(sys.stdin.readline())

cache = []

i = 2

while M != 1:
    if M % i == 0:
        print(i)
        M = M / i
    else:
        i += 1