# https://www.acmicpc.net/problem/13549
# 숨바꼭질 3
import sys
import heapq

input = sys.stdin.readline
INF = int(1e10)
MAX = 200_000

# N, K = map(int, input().split())
N, K = 5, 17
# N, K = 20, 17

if N >= K:
    print(print(N - K))
    exit()

# graphs = [[] for _ in range(K+1)]
# distances = [INF] * (K + 1)

graphs = [[] for _ in range(MAX)]
distances = [INF] * MAX

# for i in range(K + 1):
for i in range(MAX):
    graphs[i].append((i + 1, 1))
    graphs[i].append((i * 2, 0))

    if i > 0:
        graphs[i].append((i - 1, 1))

distances[N] = 0
q = []
heapq.heappush(q, (0, N))

# print(graphs)
while q:
    current_weight, now = heapq.heappop(q)

    if current_weight > distances[now]:
        continue

    for next_node, next_weight in graphs[now]:
        cost = current_weight + next_weight

        # if next_node <= K and distances[next_node] > cost:
        if 0 <= next_node <= MAX - 1 and distances[next_node] > cost:
            distances[next_node] = cost
            heapq.heappush(q, (cost, next_node))

print(distances)
print(distances[K])


