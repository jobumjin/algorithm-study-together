import sys

putNum = sys.stdin.readline

size, target = input().split()
size = int(size)
target = int(target)

total = 0
s = []

for _ in range(size):
    s.append(int(putNum()))

while len(s) > 0:
    term = int((target / s[-1]))
    if term > 0:
        total += term
        target = target - (s[-1] * term)
        if target == 0:
            break

    s.pop(-1)

print(total)
