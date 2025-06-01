# https://www.acmicpc.net/problem/16236
# 아기 상어
import sys
from collections import deque

input = sys.stdin.readline

INF = int(1e10)
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find(arr, n, current, level, visited):
    x, y = INF, INF
    visited[current[0]][current[1]] = 0

    need_visited = deque([current])
    while need_visited:
        current_x, current_y = need_visited.popleft()

        for dx, dy in DIRECTIONS:
            row, col = current_x + dx, current_y + dy

            if 0 <= row < n and 0 <= col < n and level >= arr[row][col] and visited[row][col] == 0:
                visited[row][col] = visited[current_x][current_y] + 1
                need_visited.append((row, col))

                if arr[row][col] != 0 and level > arr[row][col]:
                    if (x, y) == (INF, INF):
                        x, y = row, col
                    if visited[x][y] >= visited[row][col]:
                        if x >= row and y >= col:
                            x, y = row, col

                        if x > row:
                            x, y = row, col

    if x == INF or y == INF:
        return INF, x, y
    else:
        return visited[x][y], x, y


N = int(input())
graphs = [[] for _ in range(N)]
now = (INF, INF)

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        graphs[i].append(line[j])
        if line[j] == 9:
            now = (i, j)
            graphs[i][j] = 0

level = 2
count = 0
time = 0
while True:
    if count == level:
        count = 0
        level += 1

    visited = [[0] * N for _ in range(N)]
    distance, next_x, next_y = find(graphs, N, now, level, visited)
    count += 1
    if (next_x, next_y) == (INF, INF):
        print(time)
        break

    graphs[next_x][next_y] = 0
    time += distance
    now = (next_x, next_y)