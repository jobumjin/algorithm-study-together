from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    if right_index - left_index == 0:
        return -1
    else:
        return right_index - left_index

n, m = map(int, input().split()) # n  을 어디다 쓰지 않는 것 같아서 잘 모르겠다.

array = list(map(int, input().split()))
print(count_by_range(array, m, m))