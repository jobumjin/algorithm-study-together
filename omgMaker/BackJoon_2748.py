def solution(num):
    if num == 0 or num == 1:
        return num

    return solution(num - 1) + solution(num - 2)


target = int(input())


print(solution(target))
