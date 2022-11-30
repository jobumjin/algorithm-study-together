n = input()
x = list(map(int,input().split()))

group = 0  # 그룹 수
count = 0 # 그룹에 포함된 모험가 수
x.sort() # 정렬

for i in x: #공포도가 낮은 모험가부터 하나씩 확인하기
    count += 1 # 그룹에 해당하는 모험가 추가
    if count >= i: # 모험가 수가 공포도와 크거나 같은지 확인
        group += 1 # 크거나 같으면 그룹 추가
        count = 0 # 모험가수 초기화

print(group)

'''
입력값 : 2 1 3 2 2 
결과값 : 2
'''
