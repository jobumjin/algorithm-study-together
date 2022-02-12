import sys

i = 0


def is_big(d, r1):
    if d > r1:
        return r1
    else:
        return d


while True:
    i += 1
    r1, r2, r3 = map(int, sys.stdin.readline().split())
    if r1 + r2 + r3 == 0:
        break
    else:
        result = (r1 * int(r3 / r2)) + is_big(r3 % r2, r1)
        print('Case ' + str(i) + ': ' + str(result))

# test