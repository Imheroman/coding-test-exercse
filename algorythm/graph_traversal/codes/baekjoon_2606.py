# https://www.acmicpc.net/problem/2606
# 바이러스
# 아주 조금 참고 블로그: https://bio-info.tistory.com/152 / count 대신 sum(visited) 참고

# DFS code
from collections import deque
from sys import stdin

input = stdin.readline

N = int(input())
E = int(input())

graph = [set() for _ in range(N + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

visited = [0] * (N + 1)
visited[1] = 1
need_visited = deque([1])

while need_visited:
    current = need_visited.pop()
    if visited[current] == 0:
        visited[current] = 1

    for node in graph[current]:
        if visited[node] == 0:
            visited[node] = 1
            need_visited.extend(graph[node])

print(sum(visited) - 1)

# BFS code
# N = int(input())
# E = int(input())
#
# graph = [[] for _ in range(N + 1)]
#
# for _ in range(E):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# visited = [0] * (N + 1)
# visited[1] = 1
# need_visited = deque([1])
#
# while need_visited:
#     current = need_visited.popleft()
#
#     for node in graph[current]:
#         if visited[node] == 0:
#             visited[node] = 1
#             need_visited.append(node)
#
# print(sum(visited) - 1)

# my code
# from collections import deque
# from sys import stdin
#
# input = stdin.readline
#
# N = int(input())
# E = int(input())
#
# graph = [[] for _ in range(N + 1)]
#
# for _ in range(E):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# visited = [False] * (N + 1)
# visited[1] = True
# need_visited = deque([1])
#
# count = 0
# while need_visited:
#     current = need_visited.popleft()
#
#     for node in graph[current]:
#         if not visited[node]:
#             need_visited.append(node)
#             count += 1
#             visited[node] = True
#
# print(count)
