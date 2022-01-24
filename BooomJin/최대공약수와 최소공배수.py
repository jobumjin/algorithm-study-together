def solution(n, m):
    answer = []
    a = []
    for i in range(1,n+1):
        if n % i == 0 and m % i == 0:
            a.append(i)
    answer.append(a[-1])
    b = n / a[-1] * m / a[-1] * a[-1]
    answer.append(int(b))
    return answer

n = 8
m = 12
print(solution(n,m))

# while 문
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))