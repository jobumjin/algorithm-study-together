import sys

N = int(sys.stdin.readline())

arr = list(map(int, input().split()))

count = 0
for i in range(len(arr)):
    target = arr[i]

    if target == 1:
        continue
    elif target == 2 or target == 3:
        count += 1
    else:
        if target % 2 == 0 or target % 3 == 0:
            continue
        else:
            j = 2
            tf = True
            while j < int(target/2)+1:
                if target % j == 0:
                    tf = False
                    break
                j += 1

            if tf:
                count += 1

print(count)
