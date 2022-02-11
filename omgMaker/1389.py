import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

board = [[0] * N for _ in range(N)]
board_result = [[-1] * N for _ in range(N)]
chk = [False for _ in range(N)]

for _ in range(M):
    r1, r2 = map(int, sys.stdin.readline().split())
    board[r1 - 1][r2 - 1] = 1
    board[r2 - 1][r1 - 1] = 1


def bfs():
    for i in range(N):
        for j in range(N):
            chk[j] = False

        q = deque()
        chk[i] = True
        q.append((i, 0))

        while q:

            x, count = q.popleft()
            board_result[i][x] = count
            board_result[x][i] = count
            if all(board_result[i]):
                break

            for k in range(N):
                if board[x][k] == 1 and not chk[k]:
                    chk[k] = True
                    q.append((k, count + 1))


bfs()

minn = sum(board_result[0])
min_num = 0

for l in range(N):
    term_min = sum(board_result[l])
    if term_min < minn:
        minn = term_min
        min_num = l

print(min_num+1)
