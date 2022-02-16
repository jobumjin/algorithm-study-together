import sys
import heapq

s = sys.stdin.readline().strip()

arr = []

for i in range(len(s)):
    heapq.heappush(arr, - int(s[i]))

result = ''
while len(arr) > 0:
    result += str(-1 * heapq.heappop(arr))

print(result)