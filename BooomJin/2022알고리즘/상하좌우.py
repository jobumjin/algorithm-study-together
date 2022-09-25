n = int(input())
plan = list(map(str, input().split()))
x, y = 1, 1

for i in plan:
    if i == "R":
        y += 1
        if y > n:
            y -= 1
    elif i == "L":
        y -= 1
        if y < 1:
            y += 1
    elif i == "U":
        x -= 1
        if x < 1:
            x += 1
    else:
        x += 1
        if x > n:
            x -= 1

print(x, ",",y)