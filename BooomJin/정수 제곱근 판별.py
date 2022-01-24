def solution(n):
    a = 0
    if n ** (1 / 2) % 1 == 0:
        a = (n ** (1 / 2) + 1) ** 2
    else:
        a = -1
    return a

#math library 사용
import math
def nextSqure(n):
    # 함수를 완성하세요
    return 'no' if not math.sqrt(n).is_integer() else (math.sqrt(n)+1)**2