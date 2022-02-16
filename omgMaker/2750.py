import sys
import heapq

N = int(sys.stdin.readline())

arr = []

for i in range(N):
    heapq.heappush(arr, int(sys.stdin.readline()))

while len(arr) > 0:
    print(heapq.heappop(arr))
