n = int(input())
# 부모 테이블
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

# find, union 연산
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: # b -> a로 연결
        parent[b] = a
    else:
        parent[a] = b

# 각 행성의 좌표 입력받기
x = []
y = []
z = []
for i in range(1, n+1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))
# 각 좌표 낮은 순으로 정렬
x.sort(); y.sort(); z.sort()

# 거리(간선 비용) 계산 후 간선 정보 저장
edges = []
for i in range(n-1):
    edges.append((x[i+1][0]-x[i][0], x[i+1][1], x[i][1]))
    edges.append((y[i+1][0]-y[i][0], y[i+1][1], y[i][1]))
    edges.append((z[i+1][0]-z[i][0], z[i+1][1], z[i][1]))
# 이번엔 간선 비용 순으로 정렬
edges.sort()
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)

print(result)