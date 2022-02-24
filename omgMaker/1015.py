import sys

T = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

cache = [-1 for _ in range(max(arr))]
cache_2 = [0 for _ in range(max(arr))]

arr_sort = arr.copy()
arr_sort.sort()

for i in range(T):
    if cache[arr_sort[i] - 1] == -1:
        cache[arr_sort[i] - 1] = i

result = ''
for i in range(T):
    result += str(cache[arr[i] - 1]) + ' '
    cache[arr[i] - 1] += 1

print(result)
