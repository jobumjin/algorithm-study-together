import heapq
INF = int(1e9)

# 좌표 설정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 입력값 받기
test_case = int(input())
for _ in range(test_case):
  n = int(input())
  graph = []
  for i in range(n):
    graph.append(list(map(int, input().split())))

# 최단거리 테이블 초기화
distance = [[INF] * n for _ in range(n)]

# 시작노드값에 관한 정보 초기화
x, y = 0, 0
q = [(graph[x][y], x, y)]
distance[x][y] = graph[x][y]

# 알고리즘 수행
while q:
  dist, x, y = heapq.heappop(q)
  if distance[x][y] < dist:
    continue
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
    cost = dist + graph[nx][ny]
    if cost < distance[nx][ny]:
      distance[nx][ny] = cost
      heapq.heappush(q, (cost, nx, ny))

print(distance[n - 1][n - 1])