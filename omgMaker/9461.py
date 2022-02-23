N = int(input())

targets = []

for i in range(N):
    targets.append(int(input()))

Max = max(targets)
cache = [0 for _ in range(Max)]

for i in range(Max):
    if i == 0 or i == 1 or i == 2:
        cache[i] = 1
    elif i == 3 or i == 4:
        cache[i] = 2
    else:
        cache[i] = cache[i - 5] + cache[i - 1]

for i in range(N):
    print(cache[targets[i] - 1])