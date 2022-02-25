import sys

# 제목 : 숫자 정사각형

# N×M크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다.
# 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오.
# 이때, 정사각형은 행 또는 열에 평행해야 한다.

# 예제 입력
# 3 5
# 42101
# 22100
# 22101

# 예제 출력
# 9

# T = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
N, M = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

print(board)

Max = 0
for t in range(1, min(N, M)+1):  # 가로나 세로 크기중 작은쪽
    for i in range(N - t):
        for j in range(M - t):

            r1 = board[i][j]
            r2 = board[i][j + t]
            r3 = board[i + t][j]
            r4 = board[i + t][j + t]

            if r1 == r2 == r3 == r4 and Max < t:
                Max = t

print((Max + 1) ** 2)
