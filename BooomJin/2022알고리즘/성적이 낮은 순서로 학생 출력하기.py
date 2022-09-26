n = int(input())

array = []

for i in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))

array = sorted(array)
    
for i in array:
    print(i[0], end = " ")