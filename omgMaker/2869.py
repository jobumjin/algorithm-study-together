import sys

N, M, C = map(int, sys.stdin.readline().split())

C -= M
term = N - M

if C % term == 0:
    print(int(C / term))
else:
    print(int(C / term) + 1)