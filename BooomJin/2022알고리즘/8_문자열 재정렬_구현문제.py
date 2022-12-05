data = input()
result = []
value = 0

# 문자를 하나씩 확인
for x in data:
    #알파벳
    if x.isalpha():
        result.append(x)
    #숫자
    else:
        value += int(x)

result.sort()

# 숫자가 하나라도 존재하는경우 가장뒤에 삽입
if value != 0:
    result.append(str(value))

print(''.join(result))