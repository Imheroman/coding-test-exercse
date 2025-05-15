# https://www.acmicpc.net/problem/1916
# 최소비용 구하기
import sys
import heapq

input = sys.stdin.readline
INF = int(1e10)

N = int(input())
M = int(input())

graphs = [[] for _ in range(N+1)]

for _ in range(M):
    _from, _to, weight = map(int, input().split())
    graphs[_from].append((_to, weight))

A, B = map(int, input().split())

distances = [INF for _ in range(N+1)]
distances[A] = 0
q = []
heapq.heappush(q, (0, A))

while q:
    now_cost, current = heapq.heappop(q)

    if distances[current] < now_cost:  # 현재 방문한 노드의 비용이 기존에 방문했던 노드들의 비용보다 값이 크면 continue
        continue

    for next_node, next_cost in graphs[current]:  # 현재 노드에서 방문할 수 있는 노드들에 대해 반복
        cost = next_cost + now_cost  # 현재 노드의 값과 이동할 노드의 값 계산

        if distances[next_node] > cost:  # 기존의 노드를 방문할 수 있는 값보다 이동해서 가는 값이 더 작으면
            distances[next_node] = cost  # 값 업데이트
            heapq.heappush(q, (cost, next_node))  # 다음 노드로 다시 방문

print(distances[B])