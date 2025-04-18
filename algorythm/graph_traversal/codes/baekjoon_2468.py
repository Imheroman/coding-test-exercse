# https://www.acmicpc.net/problem/2468
# 안전 영역
import sys
from collections import deque

input = sys.stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N = int(input())
graphs = [list(map(int, input().split())) for _ in range(N)]


def bfs(g, visit, start, h):
    need_visited = deque([start])

    while need_visited:
        x, y = need_visited.popleft()
        for dx, dy in DIRECTIONS:
            row, col = x + dx, y + dy
            if (0 <= row < N and 0 <= col < N and
                    (h < g[row][col]) and not visit[row][col]):
                visit[row][col] = True
                need_visited.append((row, col))


answer = 1
for height in range(100):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and height < graphs[i][j]:
                bfs(graphs, visited, (i, j), height)
                count += 1
    answer = max(answer, count)

print(answer)

