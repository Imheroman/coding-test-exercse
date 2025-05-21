# https://www.acmicpc.net/problem/1260
# DFS와 BFS
# 참고와 이해만한 블로그: https://ji-gwang.tistory.com/291
from sys import stdin
from collections import deque

input = stdin.readline


def dfs(graph, current, visited):
    visited[current] = True
    print(current, end=" ")

    for value in graph[current]:
        if not visited[value]:
            dfs(graph, value, visited)


def bfs(graph, s):
    visited = deque([s])
    need_visit = deque([s])

    while need_visit:
        current = need_visit.popleft()

        for value in graph[current]:
            if value not in visited:
                visited.append(value)
                need_visit.append(value)

    return visited


# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4


V, E, start_node = map(int, input().split())
queue = deque([] for _ in range(V + 1))

for _ in range(E):
    start, to = map(int, input().split())
    queue[start].append(to)

    if start not in queue[to]:
        queue[to].append(start)

for q in queue:
    if q:
        q.sort()

dfs(queue.copy(), start_node, [False] * (V + 1))
print()
print(*bfs(queue.copy(), start_node), sep=" ")
