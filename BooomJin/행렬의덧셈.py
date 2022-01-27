def solution(arr1, arr2):
    answer = []
    result = []
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            result.append(arr1[i][j]+arr2[i][j])
        answer.append(result)
        result = []
    return answer

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

print(solution(arr1,arr2))

## 함수를 활용하자..
def sumMatrix(A,B):
    return [list(map(sum, zip(*x))) for x in zip(A, B)]