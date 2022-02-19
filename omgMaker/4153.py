import sys

while True:
    arr = list(map(int, input().split()))
    if arr.count(0) == 3:
        break
    else:
        Mx = max(arr)

        arr.remove(Mx)

        if Mx ** 2 == (arr[0] ** 2) + (arr[1] ** 2):
            print('right')
        else:
            print('wrong')

