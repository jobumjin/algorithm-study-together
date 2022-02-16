N = int(input())

arr = [[] for _ in range(20000)]

cache = []

for i in range(N):
    term = input()
    if term not in arr[len(term) - 1]:
        arr[len(term)-1].append(term)
        if len(term)-1 not in cache:
            cache.append(len(term)-1)

cache.sort()

for cac in cache:
    if len(arr[cac]) > 0:
        arr[cac].sort()
        for j in range(len(arr[cac])):
            print(arr[cac][j])
