# https://www.acmicpc.net/problem/10282
# 해킹
import heapq
import sys

input = sys.stdin.readline
INF = int(1e10)


def dijkstra(graph, size, start):
    distances = [INF] * (size + 1)
    distances[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        current_weight, now = heapq.heappop(q)

        if distances[now] < current_weight:
            continue

        for next_node, next_weight in graph[now]:
            cost = next_weight + current_weight
            if distances[next_node] > cost:
                distances[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    computers = 0
    time = 0
    for distance in distances:
        if distance == INF:
            continue

        computers += 1
        time = max(time, distance)

    print(computers, time)


T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    graphs = [[] * (n + 1) for _ in range(n + 1)]

    for _ in range(d):
        _to, _from, weight = map(int, input().split())
        graphs[_from].append((_to, weight))

    dijkstra(graphs, n, c)