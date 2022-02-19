import sys

t = int(input())

cache = []
for i in range(t):
    cache.append(int(sys.stdin.readline()))

Max = max(cache)

c = [True for _ in range(Max + 1)]

for i in range(2, Max + 1):  # 일단 (2 * Max) 까지 소수를 구해둠
    if c[i]:
        for j in range(i * 2, Max + 1, i):
            c[j] = False

for i in range(t):
    term = int(cache[i] / 2)
    if not c[term]:
        for j in range(term - 1, 1, -1):
            if c[j] and c[cache[i] - j]:
                print(j, cache[i] - j)
                break
    else:
        print(term, term)
