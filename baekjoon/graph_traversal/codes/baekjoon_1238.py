# https://www.acmicpc.net/problem/1238
# 파티
import sys
import heapq

input = sys.stdin.readline
INF = int(1e10)

N, M, X = map(int, input().split())
graphs = [[] for _ in range(N+1)]

for _ in range(M):
    _from, _to, time = map(int, input().split())
    graphs[_from].append((_to, time))

distances = [[INF] * (N + 1) for _ in range(N+1)]

for student in range(1, N+1):
    distances[student][student] = 0
    q = []
    heapq.heappush(q, (0, student))

    while q:
        current_weight, now = heapq.heappop(q)

        if distances[student][now] < current_weight:
            continue

        for next_node, next_weight in graphs[now]:
            cost = next_weight + current_weight
            if distances[student][next_node] > cost:
                distances[student][next_node] = cost
                heapq.heappush(q, (cost, next_node))

answer = -1
for student in range(1, N + 1):
    if student == X:
        continue

    result = distances[student][X] + distances[X][student]
    answer = max(answer, result)

print(answer)
