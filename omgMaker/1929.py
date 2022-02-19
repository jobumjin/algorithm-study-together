import sys

M, N = map(int, sys.stdin.readline().split())

c = [True for _ in range(N+1)]

#  내가 평소에 자주 사용하던 if i > N/2 의 방법은 많은 양의 소수를 판별하는데엔 적합하지 않음.
#  이전에 얻은 정보를 이요해서 이후에 행하는 연산을 편하게 만들고 밑작업을 끝마친 후,
#  O(1) 시간복잡도로 문제를 해결하는 방법이 좋을때가 많음.
for i in range(2, N+1):
    if c[i]:
        for j in range(i * 2, N+1, i):
            c[j] = False

if M == 1:
    for i in range(2, N + 1):
        if c[i]:
            print(i)
else:
    for i in range(M, N+1):
        if c[i]:
            print(i)
