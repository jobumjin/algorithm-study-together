import sys

arr = list(map(int,sys.stdin.readline().split()))

if arr[0] == 1:
    for i in range(8):
        if arr[i] != i + 1:
            print('mixed')
            break

        if arr[i] == 8 and i == 7:
            print('ascending')

elif arr[0] == 8:
    for i in range(8):
        if arr[i] != 8 - i:
            print('mixed')
            break

        if arr[i] == 1 and i == 7:
            print('descending')
else:
    print('mixed')