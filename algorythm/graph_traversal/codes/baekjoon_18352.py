# https://www.acmicpc.net/problem/18352
# 특정 거리의 도시 찾기
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, M, K, X = map(int, input().split())
graphs = [[] for _ in range(N + 1)]

for _ in range(M):
    _from, _to = map(int, input().split())
    graphs[_from].append((_to, 1))

distance = [INF] * (N + 1)
distance[X] = 0  # 시작 지점 거리 초기화
answer = []
need_visited = []  # 방문할 노드들 저장
heapq.heappush(need_visited, (0, X))  # q에 cost(0)과 시작 지점 X를 넣음
while need_visited:  # 다익스트라 시작
    dist, now = heapq.heappop(need_visited)  # 방문해야 할 노드 꺼냄

    if distance[now] == K:  # 조건에 만족하는 노드면 정답에 포함
        answer.append(now)

    if distance[now] < dist:  # 기존 거리보다 거쳐가는 값이 더 크면, continue(pass)
        continue

    # 기존 거리보다 거쳐가는 비용이 더 적은 경우에
    for node, value in graphs[now]:  # 지금 방문할 수 있는 노드들을 탐색(노드와 가중치를 같이 꺼냄)
        cost = dist + value  # 지금 노드와 다음에 방문할 노드를 거쳐 가는 경우의 값을 계산
        if distance[node] > cost:  # 지금 저장된 거리보다 노드를 거쳐가는 경우의 값이 더 작은 경우에
            distance[node] = cost  # 값 업데이트
            heapq.heappush(need_visited, (cost, node))  # 노드 다시 방문

if answer:
    print(*answer, sep='\n')
else:
    print(-1)