N = int(input())

cache = [-1 for i in range(N+1)]

cache[0] = 0
cache[1] = 1
if N > 1:
    cache[2] = 2


def solution(n):
    count = 3
    while True:
        cache[count] = cache[count - 2] + cache[count - 1]

        if count == n:
            return cache[count]
        else:
            count += 1


if N <= 2:
    print(cache[N])
else:
    print(int(solution(N) % 10007))
