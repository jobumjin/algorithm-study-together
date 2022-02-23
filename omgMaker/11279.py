import sys
import heapq
pq = []

N = int(sys.stdin.readline())

for i in range(N):
    term = int(sys.stdin.readline())
    if term == 0:
        if len(pq) != 0:
            print(-1 * heapq.heappop(pq))
        else:
            print(0)
    else:
        heapq.heappush(pq, -term)
