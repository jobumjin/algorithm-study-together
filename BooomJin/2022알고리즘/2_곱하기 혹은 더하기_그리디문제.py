n = input()

result = int(n[0]) #문자열 첫번째 문자를 숫자타입으로 변경

for i in range(1, len(n)):
    num = int(n[i])
    if num <= 1 or result <=1: #result와 i 중 0또는 1이 있다면 더하기 수행
        result += num
    else: # 그 외 경우 곱하기 수행
        result *= num

print(result)