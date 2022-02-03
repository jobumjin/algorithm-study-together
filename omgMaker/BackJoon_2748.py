target = int(input())

cache = [-1 for i in range(target+1)]
cache[0] = 0
cache[1] = 1


def solution(num):
    if cache[num] == -1:
        cache[num] = solution(num - 1) + solution(num - 2)

    return cache[num]


print(solution(target))
