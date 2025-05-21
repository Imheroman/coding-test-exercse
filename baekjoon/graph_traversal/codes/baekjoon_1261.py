# https://www.acmicpc.net/problem/1261
# 알고스팟
import sys
from collections import deque

input = sys.stdin.readline
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

M, N = map(int, input().split())
graphs = [list(input().rstrip()) for _ in range(N)]
# M, N = 3, 3
# graphs = [['0', '1', '1'], ['1', '1', '1'], ['1', '1', '0']]
# M, N = 4, 2
# graphs = [['0', '0', '0', '1'], ['1', '0', '0', '0']]

visited = [[-1] * M for _ in range(N)]
need_visited = deque([(0, 0)])

visited[0][0] = 0
while need_visited:
    x, y = need_visited.popleft()

    if x == N - 1 and y == M - 1:
        break

    for dx, dy in DIRECTIONS:
        row, col = x + dx, y + dy

        if 0 <= row < N and 0 <= col < M and visited[row][col] == -1:
            if graphs[row][col] == "0":
                visited[row][col] = visited[x][y]
                need_visited.appendleft((row, col))
            else:
                visited[row][col] = visited[x][y] + 1
                need_visited.append((row, col))

print(visited[N - 1][M - 1])