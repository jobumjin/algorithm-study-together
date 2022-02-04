N, M = map(int, input().split())

# cache = [[-1] * 5 for i in range(7)] 라고 입력 했을 때엔 [7][5] 배열이 선언 된다.
cache = [[-1] * (M+1) for i in range(N+1)]


def solution(n, m):
    if cache[n][m] != -1:
        return cache[n][m]

    if m == 0 or m == n:
        cache[n][m] = 1
        return 1
    elif m == 1 or m == n-1:
        cache[n][m] = n
        return n
    else:
        cache[n][m] = solution(n - 1, m - 1) + solution(n - 1, m)
        return cache[n][m]


print(int(solution(N, M) % 10007))
