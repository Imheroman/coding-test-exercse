# https://www.acmicpc.net/problem/7569
# 토마토
from collections import deque
from sys import stdin

input = stdin.readline

N, M, H = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(M * H)]
# N, M, H = 5, 3, 2
# graphs = [
#     list(map(int, "0 0 0 0 0".split())),
#     list(map(int, "0 0 0 0 0".split())),
#     list(map(int, "0 0 0 0 0".split())),
#     list(map(int, "0 0 0 0 0".split())),
#     list(map(int, "0 0 1 0 0".split())),
#     list(map(int, "0 0 0 0 0".split()))
# ]
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (M, 0), (M * -1, 0)]
row_size = H * M
need_visited = deque()
for m in range(row_size):
    for n in range(N):
        if graphs[m][n] == 1:
            need_visited.append((m, n))


def bfs(g, need):
    while need:
        x, y = need.popleft()
        for dx, dy in DIRECTIONS:
            row, col = x + dx, y + dy
            if not(dx == M or dx == M * -1):
                if not row // M == x // M:
                    continue
            if 0 <= row < row_size and 0 <= col < N and g[row][col] == 0:
                g[row][col] = 1 + g[x][y]
                need.append((row, col))


bfs(graphs, need_visited)
answer = 0
for i in range(M * H):
    for j in range(N):
        if 0 == graphs[i][j]:
            print(-1)
            exit()

        answer = max(answer, graphs[i][j] - 1)

for graph in graphs:
    print(graph)

print(answer)
