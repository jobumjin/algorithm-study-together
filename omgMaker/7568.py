#  부르트 포스, 자릿수
import sys

N = int(sys.stdin.readline())

arr = []
result = []
board = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    count = 1

    for j in range(N):
        if i != j:
            if board[i][0] < board[j][0]:
                if board[i][1] < board[j][1]:
                    count += 1
    result.append(count)

text = ''
for n in range(N):
    text += str(result[n]) + ' '
print(text)
