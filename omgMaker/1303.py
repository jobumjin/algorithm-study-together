import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [list(input().strip()) for _ in range(M)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

chk = [[False] * N for _ in range(M)]


def is_valid(y, x):
    return 0 <= y < M and 0 <= x < N


def bfs_w():
    sum_w = 0
    for i in range(M):
        for j in range(N):
            if not chk[i][j] and graph[i][j] == 'W':
                count = 1

                q = deque()
                chk[i][j] = True
                q.append((i, j))

                while q:
                    y, x = q.popleft()

                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]

                        if is_valid(ny, nx) and graph[ny][nx] == 'W' and not chk[ny][nx]:
                            chk[ny][nx] = True
                            count += 1
                            q.append((ny, nx))

                sum_w += count ** 2
    return sum_w


def bfs_b():
    sum_b = 0
    for i in range(M):
        for j in range(N):
            if not chk[i][j] and graph[i][j] == 'B':
                count = 1

                q = deque()
                chk[i][j] = True
                q.append((i, j))

                while q:
                    y, x = q.popleft()

                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]

                        if is_valid(ny, nx) and graph[ny][nx] == 'B' and not chk[ny][nx]:
                            chk[ny][nx] = True
                            count += 1
                            q.append((ny, nx))

                sum_b += count ** 2
    return sum_b


print(bfs_w(), bfs_b())
