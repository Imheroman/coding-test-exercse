# https://www.acmicpc.net/problem/5972
# 택배 배송
import heapq
import sys

input = sys.stdin.readline
# DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
INF = int(1e10)

N, M = map(int, input().split())
graphs = [[] for _ in range(N + 1)]

for _ in range(M):
    _from, _to, weight = map(int, input().split())
    graphs[_from].append((_to, weight))
    graphs[_to].append((_from, weight))


def dijkstra(graph, start):
    distances = [INF] * (N + 1)
    distances[0] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        current_weight, now = heapq.heappop(q)

        if distances[now] < current_weight:
            continue

        for next_node, next_weight in graph[now]:
            cost = current_weight + next_weight

            if distances[next_node] > cost:
                distances[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    print(distances)
    print(distances[N])


dijkstra(graphs, 1)