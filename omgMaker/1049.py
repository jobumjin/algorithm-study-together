import sys

# T = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
N, M = map(int, sys.stdin.readline().split())

r1 = 1001
r2 = 1001

for i in range(M):
    term1, term2 = map(int, sys.stdin.readline().split())
    if r1 > term1:
        r1 = term1

    if r2 > term2:
        r2 = term2

if N <= 6:
    if r1 > r2 * N:
        print(r2 * N)
    else:
        print(r1)
else:
    if r1 / 6 > r2:
        print(r2 * N)
    else:
        if N % 6 == 0:
            print(r1 * int(N / 6))
        else:
            if r1 * (int(N / 6) + 1) > (r1 * int(N / 6)) + (r2 * (N % 6)):
                print((r1 * int(N / 6)) + (r2 * (N % 6)))
            else:
                print(r1 * (int(N / 6) + 1))
