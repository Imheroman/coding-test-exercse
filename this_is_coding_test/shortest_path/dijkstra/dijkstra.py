import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
DISTANCE_INDEX = 0
NODE_INDEX = 1

n, m = 6, 11  # n, m = map(int, input().split())
start = 1  # start = int(input())
graph = [[] for _ in range(n + 1)]  # 그래프 저장하기 위해 list 생성
distance = [INF] * (n + 1)  # 거리를 저장하기 위해 list 생성

# 모든 노드의 간선 입력
for _ in range(m):
    current_node_number, *connected_node_info = map(int, input().split())  # node_info: to, cost
    graph[current_node_number].append(connected_node_info)


def dijkstra(start):
    priority_queue = []
    dist = 0

    heapq.heappush(priority_queue, (dist, start))  # q에 start의 cost는 0으로 저장
    distance[start] = dist

    while priority_queue:
        dist, node = heapq.heappop(priority_queue)  # 최단 거리가 가장 짧은 node index 꺼내기

        if distance[node] < dist:  # distance에 저장된 노드의 길이가 dist보다 더 작으면 continue
            continue

        for node in graph[node]:
            current_distance = dist + node[NODE_INDEX]

            if current_distance < distance[node[DISTANCE_INDEX]]:  # 현재의 길이보다 기존에 저장된 길이가 더 크면
                distance[node[DISTANCE_INDEX]] = current_distance  # 길이를 변경하고
                heapq.heappush(priority_queue, (current_distance, node[DISTANCE_INDEX]))  # 현재 길이와 노드 저장

dijkstra(start)

result = []
for index in range(1, n + 1):
    if distance[index] == INF:
        result.append("INFINITY")
    else:
        result.append(distance[index])

print(*result)
