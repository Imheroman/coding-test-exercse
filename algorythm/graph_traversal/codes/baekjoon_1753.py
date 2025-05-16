# https://www.acmicpc.net/problem/1753
# 최단경로
import sys

input = sys.stdin.readline
INF = int(1e10)

V, E = map(int, input().split())
K = int(input())
graphs = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graphs[u].append((v, w))

distances = [INF] * (V + 1)
visited = [False] * (V + 1)


def get_smallest_index():
    smallest = INF
    index = 0

    for i in range(1, V + 1):
        if distances[i] < smallest and not visited[i]:
            smallest = distances[i]
            index = i

    return index


def dijkstra(start):
    distances[start] = 0
    visited[start] = True

    for node, weight in graphs[start]:  # start가 방문할 수 있는 모든 노드들에 대해 이동 값 초기화 (후에 인덱스를 결정하기 위함도 있음)
        distances[node] = weight

    for i in range(V - 1):  # 시작 노드는 방문할 필요 없으니까 n - 1
        current = get_smallest_index()  # 가중치가 가장 작은 인덱스를 찾아냄
        visited[current] = True

        for node, weight in graphs[current]:
            cost = weight + distances[current]
            if distances[node] > cost:
                distances[node] = cost


dijkstra(K)

for now in range(1, len(distances)):
    if distances[now] == INF:
        print("INF")
    else:
        print(distances[now])