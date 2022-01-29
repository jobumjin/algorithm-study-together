import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

board = [input() for _ in range(N)]

print(board)

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


chk = [[False] * M for _ in range(N)]


def is_valid(y, x):
    return 0 <= y < N and 0 <= x < M


# 평소와 다르게 x,y 순서가 아닌 y,x 순서로 대입하는 이유 :
# 평소에 적던 x,y 는 array[i][j] 의 대체같은 느낌으로 사용되어 x=i, y=j 의 느낌으로 x,y 로 사용했지만,
# 미로탐색 같은 좌표와 관련된 문제를 풀 때에 x,y 를 사용하게 되면 보통 위치 좌표를 나타낼때의 x,y 의 의미가 먼저 떠오르게 되므로
# 애초부터 array[y][x] 로 사용하는 편이 y=세로 위치, x= 가로 위치 라는 의미에서 더 알맞음

# BFS 문제를 다룰 때엔 너무 깊이 생각할 필요가 없음. 어차피 최대 시간 복잡도가 N * M 에서 멈추게 되는 부분을 꼭 기억하기.
# 어떻게 해야 이전 노드로 돌아가서 다시 다음 방향을 찾지? 같은 생각을 할 필요가 없음. 어차피 도중에 목적지에 도달하는게 아니라면 지나갈 수 있는 길은 다 지나가게 돼있음.

def bfs():
    q = deque()
    chk[0][0] = True
    q.append((0, 0, 1))

    while q:
        y, x, count = q.popleft()

        if y == N - 1 and x == M - 1:
            return count

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx] = True
                q.append((ny, nx, count+1))

    return -1


print(bfs())
