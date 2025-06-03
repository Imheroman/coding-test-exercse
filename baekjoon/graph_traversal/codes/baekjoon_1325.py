# https://www.acmicpc.net/problem/1325
# 효율적인 해킹
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
relationships = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    relationships[b].append(a)

_max = 0
answer = []


def bfs(arr, n, start):
    visited = [False] * (n + 1)
    visited[start] = True
    need_visited = deque([start])
    count = 1
    while need_visited:
        now = need_visited.popleft()

        for node in arr[now]:
            if not visited[node]:
                visited[node] = True
                need_visited.append(node)
                count += 1

    return count


for current in range(1, N + 1):
    if len(relationships[current]) == 0:
        continue

    result = bfs(relationships, N, current)

    if result == _max:
        answer.append(current)
    elif result > _max:
        _max = result
        answer.clear()
        answer.append(current)

print(*answer)