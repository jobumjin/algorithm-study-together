def solution(n):
    answer = list(map(int,str(n)))
    return list(reversed(answer))

n = 1234553275437
print(solution(n))

## reversed 안쓰고 풀기
def digit_reverse(n):
    return list(map(int, list(str(n))[::-1]))