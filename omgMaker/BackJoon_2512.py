N = int(input())

arr = list(map(int, input().split()))

total = int(input())

arr.sort()

sumArr = sum(arr)

over = 0

if sumArr <= total:
    print(arr[-1])
else:
    for i in range(N):
        if arr[i] <= total/(N-i):
            total -= arr[i]
        else:
            over = i
            break
    print(int(total/(N - over)))