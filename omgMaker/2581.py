import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

cache = []

for i in range(1, M):  # M 이전까지의 소수를 다 구하기
    if i == 1:
        continue
    elif i == 2:
        cache.append(i)
    else:
        if i % 2 == 0:
            continue

        else:
            tf = True
            for j in range(len(cache)):
                if int(i / 2) < cache[j]:
                    break
                else:
                    if i % cache[j] == 0:
                        tf = False
                        break
            if tf:
                cache.append(i)

size1 = len(cache)

for i in range(M, N+1):  # M 이전까지의 소수를 다 구하기
    if i == 1:
        continue
    elif i == 2:
        cache.append(i)
    else:
        if i % 2 == 0:
            continue

        else:
            tf = True
            for j in range(len(cache)):
                if int(i / 2) < cache[j]:
                    break
                else:
                    if i % cache[j] == 0:
                        tf = False
                        break
            if tf:
                cache.append(i)

if size1 == len(cache):
    print(-1)
else:
    print(sum(cache[size1:]))
    print(cache[size1])
