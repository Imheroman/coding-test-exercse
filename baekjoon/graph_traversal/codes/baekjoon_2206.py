# https://www.acmicpc.net/problem/2206
# 벽 부수고 이동하기
import sys
from collections import deque

input = sys.stdin.readline
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
INF = int(1e10)

N, M = map(int, input().split())
graphs = [list(map(int, list(input().rstrip()))) for _ in range(N)]
# N, M = 6, 4
# graphs = [
#     list(map(int, list("0100"))),
#     list(map(int, list("1110"))),
#     list(map(int, list("1000"))),
#     list(map(int, list("0000"))),
#     list(map(int, list("0111"))),
#     list(map(int, list("0000"))),
# ]


def bfs(graph, n, m, size, start=(0, 0)):
    x, y = start
    if size == 0 or (x == n - 1 and y == m - 1):
        visited = [[0] * M for _ in range(N)]
        visited[0][0] = 1
        need_visited = deque([(0, 0)])
        while need_visited:
            r, c = need_visited.pop()

            for dx, dy in DIRECTIONS:
                row, col = r + dx, c + dy

                if 0 <= row < n and 0 <= col < m and visited[row][col] == 0:
                    if graph[row][col] == 0:
                        visited[row][col] = visited[r][c] + 1
                        need_visited.append((row, col))

        # print(visited)
        return visited[n - 1][m - 1]

    result = INF
    for i in range(n):
        for j in range(m):
            # print(graph)
            # print(f"i: {i}, j: {j}", end=" -> ")
            origin = graph[i][j]
            graph[i][j] = 0
            res = bfs(graph, n, m, size - 1, (i, j))
            if res != 0:
                result = min(result, res)
            graph[i][j] = origin

    return result


answer = bfs(graphs, N, M, 1)

if answer == INF:
    print(-1)
else:
    print(answer)
