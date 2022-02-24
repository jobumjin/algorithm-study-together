import sys
import math

T = int(sys.stdin.readline())

results = []
N_and_M = []

for i in range(T):
    N_and_M.append(list(map(int, sys.stdin.readline().split())))

for i in range(T):
    N = N_and_M[i][0]
    M = N_and_M[i][1]
    results.append(int(math.factorial(M) / (math.factorial(M - N) * math.factorial(N))))

for i in range(T):
    print(results[i])
