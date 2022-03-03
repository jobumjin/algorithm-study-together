import sys

max_num = -1
max_sum = 0

for i in range(5):
    arr = list(map(int,sys.stdin.readline().split()))
    if max_sum < sum(arr):
        max_sum = sum(arr)
        max_num = i + 1

print(max_num, max_sum)
