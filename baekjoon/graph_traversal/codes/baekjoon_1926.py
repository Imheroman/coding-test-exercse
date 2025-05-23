# https://www.acmicpc.net/problem/1926
# 그림
import sys
from collections import deque

input = sys.stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N, M = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(N)]


def bfs(start):
    size = 1

    need_visited = deque([start])
    while need_visited:
        x, y = need_visited.popleft()
        for dx, dy in DIRECTIONS:
            row, col = x + dx, y + dy

            if (0 <= row < N and 0 <= col < M) and graphs[row][col] == 1:
                size += 1
                need_visited.append((row, col))
                graphs[row][col] = 0

    return size


count = 0
max_size = 0
for i in range(N):
    for j in range(M):
        if graphs[i][j] == 1:
            count += 1
            graphs[i][j] = 0
            max_size = max(bfs((i, j)), max_size)

print(count)
print(max_size)
