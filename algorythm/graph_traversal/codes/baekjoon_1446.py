# https://www.acmicpc.net/problem/1446
# 지름길
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

N, D = map(int, input().split())
graphs = [[] for num in range(D + 1)]

for i in range(D):
    graphs[i].append((i+1, 1))  # 현재 그래프에서 갈 수 있는 곳을 저장한다. D 까지만 하는 이유는 D는 목적지이기 때문에, 다음 방향이 없어야 하기 때문이다.

for _ in range(N):
    start, destination, weight = map(int, input().split())
    if destination <= D:  # 목적지가 고속도로의 길이보다 짧은 것만 그래프에 추가한다.
        graphs[start].append((destination, weight))

distance = [INF] * (D + 1)  # 출발지로부터의 거리를 측정한다.
distance[0] = 0  # 출발지는 거리를 0으로 설정한다.
q = []  # 이동할 목적지들을 저장하는 곳
heapq.heappush(q, (0, 0))  # 처음 시작지를 추가
while q:  # 방문해야 할 그래프들이 있다면
    w, now = heapq.heappop(q)  # 가중치와, 현재 방문한 인덱스를 뽑아옴

    if distance[now] < w:  # 지금 인덱스보다 가중치가 더 크면, 방문할 필요가 없음
        continue

    for node, c in graphs[now]:  # 방문할 그래프들 중
        cost = c + distance[now]  # 값을 계산하고(경유해서 가는 값)
        if distance[node] > cost:  # 지금 목적지의 값이 경유해서 가는 값보다 크다면 ? 값과 인덱스를 업데이트
            distance[node] = cost
            heapq.heappush(q, (cost, node))

print(distance[D])