# https://www.acmicpc.net/problem/2573
# 빙산
import sys
from collections import deque

input = sys.stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N, M = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(N)]


def melting_ice(arr, v, start):
    current_x, current_y = start
    count = 0
    for dx, dy in DIRECTIONS:
        row, col = current_x + dx, current_y + dy

        if 0 <= row < N and 0 <= col < M:
            if not v[row][col] and arr[row][col] == 0:
                count += 1
    return count


def count_block(arr, v):
    v[i][j] = True
    need_visited = deque([(i, j)])
    while need_visited:
        current_x, current_y = need_visited.popleft()
        for x, y in DIRECTIONS:
            r, c = current_x + x, current_y + y
            if 0 <= r < N and 0 <= c < M and arr[r][c] > 0 and not v[r][c]:
                v[r][c] = True
                need_visited.append((r, c))
    return


for year in range(100000):
    result = 0
    visit = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graphs[i][j] != 0 and not visit[i][j]:
                count_block(graphs, visit)
                result += 1

    if result > 1:
        print(year)
        exit()
    elif result == 0:
        print(0)
        exit()
    visited = [[False] * M for _ in range(N)]
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if graphs[i][j] != 0:
                visited[i][j] = True
                graphs[i][j] = max(0, graphs[i][j] - melting_ice(graphs, visited, (i, j)))

print(0)
# for graph in graphs:
#     print(graph)
