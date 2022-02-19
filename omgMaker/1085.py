import sys

x, y, w, h = map(int, sys.stdin.readline().split())

m = min(x, y, w-x, h-y)

print(m)