import sys

T = int(sys.stdin.readline())
arr_A = list(map(int, sys.stdin.readline().split()))
arr_B = list(map(int, sys.stdin.readline().split()))

arr_A.sort()
arr_B.sort()

result = 0
for i in range(T):
    result += arr_A[T - 1 - i] * arr_B[i]

print(result)