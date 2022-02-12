import sys

N, M = map(int, sys.stdin.readline().split())

s = [[] for _ in range(N)]

count = 0

for i in range(N):
    r1, r2 = map(int, sys.stdin.readline().split())

    while True:
        if len(s[r1 - 1]) == 0:  # 스택이 비어 있으면
            count += 1
            s[r1 - 1].append(r2)
        else:
            term = s[r1 - 1][-1]
            if r2 > term:
                count += 1
                s[r1 - 1].append(r2)
                break
            elif r2 < term:
                count += 1
                s[r1 - 1].pop()
            else:
                break

print(count)
