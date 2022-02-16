import sys

N = int(sys.stdin.readline())

arr = [[] for _ in range(201)]

cache = []

for i in range(N):
    age, name = input().split()
    age_int = int(age)
    arr[age_int].append(name)
    if age_int not in cache:
        cache.append(age_int)

cache.sort()

for ca in cache:
    for i in range(len(arr[ca])):
        print(ca, arr[ca][i])
