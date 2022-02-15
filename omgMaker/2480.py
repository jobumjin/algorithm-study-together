import sys

N, M, L = map(int, sys.stdin.readline().split())

if N == M == L:
    print(10000 + (N * 1000))
elif N == M or M == L or N == L:
    if N == M or N == L:
        print(1000 + (N * 100))
    else:
        print(1000 + (M * 100))
else:
    print(max(N, M, L) * 100)
