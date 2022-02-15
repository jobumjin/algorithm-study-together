#  부르트 포스, 자릿수
import sys

N, M = map(int, sys.stdin.readline().split())

board = [list(input().strip()) for _ in range(N)]

count = []


for a in range(N-7):
    for b in range(M-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        index1 += 1
                    else:
                        index2 += 1
                else:
                    if board[i][j] != 'B':
                        index1 += 1
                    else:
                        index2 += 1
        count.append(min(index1, index2))

print(min(count))