import sys

cache = []

while True:
    N = int(sys.stdin.readline())

    if N == 0:
        break
    else:
        cache.append(N)

Max = max(cache)

c = [True for _ in range((2 * Max)+1)]

for i in range(2, (2 * Max)+1):  #  일단 (2 * Max) 까지 소수를 구해둠
    if c[i]:
        for j in range(i * 2, (2 * Max)+1, i):
            c[j] = False

for i in range(len(cache)):
    count = 0
    for j in range(cache[i] + 1, (2 * cache[i]) + 1):
        if c[j]:
            count += 1
    print(count)

