# https://www.acmicpc.net/problem/11724
# 연결 요소의 개수
# BFS
# from collections import deque
# from sys import stdin
#
# input = stdin.readline
#
# N, E = map(int, input().split())
# graphs = [deque() for i in range(N + 1)]
#
# for _ in range(E):
#     n, e = map(int, input().split())
#     graphs[n].append(e)
#     graphs[e].append(n)
#
# visited = [False] * (N + 1)
# need_visited = deque()
# answer = 0
#
# for i in range(1, N + 1):  # 1 ~ N
#     if not visited[i]:
#         answer += 1
#         need_visited.append(i)
#         while need_visited:
#             current = need_visited.popleft()
#             if not visited[current]:
#                 visited[current] = True
#                 while graphs[current]:
#                     need_visited.append(graphs[current].popleft())
#
# print(answer)

# from collections import deque
# import sys
#
# sys.setrecursionlimit(10 ** 7)
# input = sys.stdin.readline
#
#
# def dfs(nodes, current, is_visited):
#     for value in nodes[current]:
#         if not is_visited[value]:
#             is_visited[value] = True
#             dfs(nodes, value, is_visited)
#
#
# N, E = map(int, input().split())
# graphs = [deque() for i in range(N + 1)]
#
# for _ in range(E):
#     n, e = map(int, input().split())
#     graphs[n].append(e)
#     graphs[e].append(n)
#
# visited = [False] * (N + 1)
# answer = 0
#
# for i in range(1, N + 1):  # 1 ~ N
#     if not visited[i]:
#         answer += 1
#         visited[i] = True
#         dfs(graphs, i, visited)
#
# print(answer)

import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def find(nodes, current):
    if nodes[current] != current:  # 최상위 노드가 아닌 경우에
        return find(nodes, nodes[current])  # 최상위 노드 탐색

    return current


def union(nodes, a, b):
    a = find(nodes, a)  # a의 최상위 노드를 찾음
    b = find(nodes, b)  # b의 최상위 노드를 찾음

    if a < b:  # 더 작은 값을 찾아서 더 큰 index에 더 작은 값 대입
        nodes[b] = a
    else:
        nodes[a] = b


N, E = map(int, input().split())
graphs = [i for i in range(N + 1)]

for _ in range(E):
    u, v = map(int, input().split())
    union(graphs, u, v)

answer = set()

for index in range(1, N + 1):
    answer.add(find(graphs, index))

print(len(answer))
