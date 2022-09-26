n = int(input())

box = []

for i in range(n):
    box.append(int(input()))
    
box = sorted(box, reverse = True)

for i in box:
    print(i, end =" ")