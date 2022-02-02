from bisect import bisect_right, bisect_left

N = int(input())
arr = sorted(map(int, input().split()))

M = int(input())
arr2 = list(map(int, input().split()))

for q in arr2:
    # bisect_right = 인덱스가 들어갈 가장 오른쪽 자리
    # bisect_left = 인덱스가 들어갈 가장 왼 자리
    # arr 내에 q 값이 없다면 위의 두 값(bisect_right, bisect_left)은 동일하다.
    if 0 < (bisect_right(arr, q) - bisect_left(arr, q)):
        print('1', end=' ')
    else:
        print('0', end=' ')

