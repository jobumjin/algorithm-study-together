n = input()

count0 = 0
count1 = 0

# 첫번째 원소 확인
if n[0] == "1":
    count0 += 1
else:
    count1 += 1

# 두번째 원소부터 차례로 확인
for i in range(len(n)-1):
    if n[i] != n[i+1]:
        if n[i+1] == '1': # 다음수에서 1로 바뀔경우
            count0 += 1
        else: #0으로 바뀔경우
            count1 += 1

print(min(count0,count1))