def solution(d, budget):
    answer = 0
    for i in sorted(d):
        budget = budget - i
        if budget >= 0:
            answer += 1
        else:
            break
    return answer


d = [2,2,3,3]
budget = 10
print(solution(d,budget))

## while문

def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)