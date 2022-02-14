import sys

# N, M = map(int, sys.stdin.readline().split())
#
# graph = [list((input().strip())) for _ in range(M)]
#
# for i in range(N):
#     for j in range(M):
#         graph[i][j] = int(graph[i][j])
#
# print(graph)
#

term = input()
size = len(term)
summ = 0


for i in range(size):
    c = ord(term[i])
    if 64 < c < 68:
        summ += 3
    elif 67 < c < 71:
        summ += 4
    elif 70 < c < 74:
        summ += 5
    elif 73 < c < 77:
        summ += 6
    elif 76 < c < 80:
        summ += 7
    elif 79 < c < 84:
        summ += 8
    elif 83 < c < 87:
        summ += 9
    elif 86 < c < 91:
        summ += 10

print(summ)