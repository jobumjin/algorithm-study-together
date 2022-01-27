def solution(x):
    hasad = sum(list(map(int,str(x))))
    if x % hasad == 0:
        answer = True
    else:
        answer = False
    return answer

x = 10
print(solution(x))

# if 문을 넣을 필요가 없네..
def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0

