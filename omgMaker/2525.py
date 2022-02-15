import sys

N, M = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())

print((N + int((M+C) / 60)) % 24, (M+C) % 60)
