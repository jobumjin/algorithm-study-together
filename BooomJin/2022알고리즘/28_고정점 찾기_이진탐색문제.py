n = int(input())
array = list(map(int, input().split()))

result = -1

for i in array:
    if array.index(i) == i:
        result = i
        break

print(result)