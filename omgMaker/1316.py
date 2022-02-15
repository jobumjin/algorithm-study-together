import sys

N = int(sys.stdin.readline())

count = 0

for i in range(N):
    s = sys.stdin.readline().strip()
    term = s[0]
    arr = []
    y_or_n = True
    for j in range(1, len(s)):
        if term != s[j]:
            if s[j] not in arr:
                arr.append(term)
                term = s[j]
            else:
                y_or_n = False
                break

    if y_or_n:
        count += 1


print(count)