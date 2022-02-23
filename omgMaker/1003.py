N = int(input())

targets = []

for i in range(N):
    targets.append(int(input()))

cache = [[0] * 2 for _ in range(max(targets)+1)]

cache[0] = [1, 0]
cache[1] = [0, 1]

for i in range(2, max(targets)+1):
    cache[i][0] = cache[i - 1][0] + cache[i - 2][0]
    cache[i][1] = cache[i - 1][1] + cache[i - 2][1]

for i in range(N):
    result = str(cache[targets[i]][0]) + ' ' + str(cache[targets[i]][1])
    print(result)
