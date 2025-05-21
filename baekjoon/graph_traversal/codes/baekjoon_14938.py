# https://www.acmicpc.net/problem/14938
# 서강그라운드
import heapq
import sys

input = sys.stdin.readline
INF = int(1e10)

N, M, R = map(int, input().split())
items = list(map(int, input().split()))

graphs = [[INF] * (N + 1) for _ in range(N + 1)]
for _ in range(R):
    _from, _to, weight = map(int, input().split())
    graphs[_from][_to] = weight
    graphs[_to][_from] = weight

for current in range(N + 1):
    graphs[current][current] = 0

for k in range(1, N + 1):  # k를 경유
    for i in range(1, N + 1):  # i에서
        for j in range(1, N + 1):  # j까지
            graphs[i][j] = min(graphs[i][j], graphs[i][k] + graphs[k][j])


answer = 0
for distances in graphs[1:]:
    total = 0
    for index in range(1, len(distances)):
        if distances[index] <= M:
            total += items[index - 1]
    answer = max(answer, total)
print(answer)