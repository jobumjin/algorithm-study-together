n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11 # 무게를 담을 수 있는 리스트
for x in data:
    array[x] += 1

result = 0
#1부터 m까지 무게 처리
for i in range(1, m+1):
    n -= array[i] #무게에 따른 볼링공 개수 제외
    result += array[i] * n #B 가 선택하는 경우의 수와 곱함

print(result)