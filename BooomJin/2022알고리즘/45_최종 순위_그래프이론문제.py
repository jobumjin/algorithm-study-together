from collections import deque

for tc in range(int(input())):
    n = int(input())
    indegree = [0] * (n+1)
    graph = [[False] * (n+1) for _ in range(n+1)]
    # 작년 순위 정보를 그래프 데이터로 변환
    data = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True  # a 순위가 b순위보다 높다면, a -> b로 연결, b입장에서 진입차수 +1
            indegree[data[j]] += 1
    # 상대적인 등수 정보 입력
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())  # 작년에 b가 더 높았는데 올해는 a가 더 높음! : a -> b로 바꾸기
        if graph[a][b]:  # graph[a][b] == True 라는 것은 a -> b를 의미하고 a 순위가 더 높음을 의미. 그러므로 b -> a로 바꾸어야 함
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[b][a] = False
            graph[a][b] = True
            indegree[a] -= 1
            indegree[b] += 1

    # 초기 진입차수 0인 노드 큐에 넣기
    queue = deque([])
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)

    result = []  # 위상정렬 결과 담을 리스트
    cycle = False  # 큐에서 n번 노드가 나오기 전에 큐의 원소 길이가 0이 되었다 = 사이클 발생 = 정렬할 수 없음(순위 알 수 없음)
    certain = True  # 매번 큐 길이를 계산할 때, 큐 길이가 2이상(원소가 2개 이상)일 때, 즉 한 번에 큐에 2개 이상 원소가 들어감 = 위상 정렬 결과가 여러개!

    for i in range(n):
        if len(queue) == 0:
            cycle = True
            break
        if len(queue) >= 2:
            certain = False
            break

        # 위상 정렬 수행
        node = queue.popleft()
        result.append(node)  # 큐에서 원소를 pop하는 순서대로 결과 = 위상정렬 결과
        # 큐에서 빼낸 노드와 연결된 노드 탐색
        for j in range(1, n+1):
            if graph[node][j]:
                indegree[j] -= 1
                # 새롭게 진입차수가 0이 된 노드 큐에 넣기
                if indegree[j] == 0:
                    queue.append(j)

    if cycle:
        print('IMPOSSIBLE')
    elif not certain:
        print('?')
    else:
        for i in result:
            print(i, end=' ')
        print()