import sys

N, M, C = map(int, sys.stdin.readline().split())

if C <= M:
    print(-1)
else:
    print(int(N /(C - M)) + 1)

# A + XB < XC
#
# A < X(C-B)
#
# A / (C-B) < X

