def solution(answers):
    answer = []
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count1 = 0
    count2 = 0
    count3 = 0
    if len(answers) // 5 > 0:
        supo1 = supo1 * (len(answers) // 5 + 1)
        supo2 = supo2 * (len(answers) // 5 + 1)
        supo3 = supo3 * (len(answers) // 5 + 1)

    for i in range(len(answers)):
        if supo1[i] == answers[i]:
            count1 += 1
        if supo2[i] == answers[i]:
            count2 += 1
        if supo3[i] == answers[i]:
            count3 += 1

    answer.append(count1)
    answer.append(count2)
    answer.append(count3)

    result = []
    for i in range(len(answer)):
        if max(answer) == answer[i]:
            result.append(i+1)
    return result

answers = [1, 2, 3, 4, 5]
answers1 = [1, 3, 2, 4, 2]

print(solution(answers))
print(solution(answers1))

## 다른사람 풀이 공간복잡도가 고려된 코드..?
from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]