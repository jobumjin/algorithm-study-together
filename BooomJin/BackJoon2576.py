answer = []
for i in range(7):
    a = int(input())
    if a % 2 == 1:
        answer.append(a)
if len(answer) == 0:
    print(-1)
else:
    print(sum(answer))
    print(min(answer))