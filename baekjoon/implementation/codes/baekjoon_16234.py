# https://www.acmicpc.net/problem/16234
# 인구 이동
import sys
from collections import deque

input = sys.stdin.readline
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(q, arr, l, r, current, visited):
    result = []
    need_visited = deque([current])

    while need_visited:
        x, y = need_visited.pop()
        visited[x][y] = True
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in result:
                if l <= abs(arr[nx][ny] - arr[x][y]) <= r:
                    result.append((nx, ny))
                    need_visited.append((nx, ny))

    if result:
        q.append(result)
    return


N, L, R = map(int, input().split())  # L 이상, R 이하
populations = [list(map(int, input().split())) for _ in range(N)]
# N, L, R = 2, 20, 50
# populations = [[50, 30], [20, 40]]
# N, L, R = 2, 40, 50
# populations = [[50, 30], [20, 40]]
# N, L, R = 2, 20, 50
# populations = [[50, 30], [30, 40]]
# N, L, R = 3, 5, 10
# populations = [[10, 15, 20], [20, 30, 25], [40, 22, 10]]
# N, L, R = 3, 34, 52
# populations = [[46, 44, 4], [33, 47, 0], [19, 35, 78]]
# N, L, R = 2, 7, 79
# populations = [[21, 8], [86, 77]]

answer = 0
while True:
    queue = []
    v = [[False] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if not v[row][col]:
                bfs(queue, populations, L, R, (row, col), v)

    if not queue:
        break

    for graph in queue:
        total = sum([populations[_x][_y] for _x, _y in graph])
        for r, c in graph:
            populations[r][c] = total // len(graph)

    answer += 1

print(answer)