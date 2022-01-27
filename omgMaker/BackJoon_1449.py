N, L = map(int, input().split())

# a = [(int(input()) + 0.5) for _ in range(N)]
a = list(map(int, input().split()))
for i in range(N):
    a[i] = a[i] + 0.5
a.sort()

end = 0.0
total = 0

for i in range(N):
    if end < a[i]:
        if 1 > (a[i] - end):
            end = end + L
            total += 1
            print('end = ', end, ', total = ', total)
        else:
            end = a[i] + (L - 1.0)
            total += 1

print(total)
