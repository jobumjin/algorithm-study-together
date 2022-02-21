import sys

N = int(sys.stdin.readline())

num_cache = list(map(int, input().split()))

cal_cache = list(map(int, input().split()))

result_cache = []

start = num_cache[0]


def solution(num, result):
    if num == len(num_cache):
        result_cache.append(result)

    else:
        for j in range(4):
            if cal_cache[j] != 0:
                cal_cache[j] -= 1
                if j == 0:
                    next_result = result + num_cache[num]
                elif j == 1:
                    next_result = result - num_cache[num]
                elif j == 2:
                    next_result = result * num_cache[num]
                else:
                    # next_result = result / num_cache[num]
                    next_result = int(result / num_cache[num])

                solution(num + 1, next_result)
                cal_cache[j] += 1


solution(1, start)

print(int(max(result_cache)))
print(int(min(result_cache)))
