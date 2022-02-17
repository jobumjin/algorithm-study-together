import sys

target = int(sys.stdin.readline())

count = 0

while True:
    if 0 < target < 3:
        count = -1
        break

    elif target == 0:
        break

    else:
        if target % 5 == 0:
            count += int(target / 5)
            break
        else:
            target -= 3
            count += 1

print(count)