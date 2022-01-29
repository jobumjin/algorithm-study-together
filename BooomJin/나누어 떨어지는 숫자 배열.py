def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    return sorted(answer)

## 더 나은 풀이보단.. 클린코드로 만드는것이 중요할 것 같다.?