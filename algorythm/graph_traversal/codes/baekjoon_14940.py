import sys
from collections import deque

input = sys.stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N, M = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
need_visited = deque()
destination = ()
for row in range(N):
    if 2 not in graphs[row]:
        continue
    col = graphs[row].index(2)
    need_visited.append((row, col))
    visited[row][col] = True
    break

answers = [[0] * M for _ in range(N)]
while need_visited:
    x, y = need_visited.popleft()

    for dx, dy in DIRECTIONS:
        r, c = x + dx, y + dy

        if 0 <= r < N and 0 <= c < M and not visited[r][c] and graphs[r][c] == 1:
            need_visited.append((r, c))
            answers[r][c] = answers[x][y] + 1
            visited[r][c] = True

for i in range(N):
    for j in range(M):
        if graphs[i][j] == 0 or visited[i][j]:
            print(answers[i][j], end=' ')
        else:
            print(-1, end=' ')
    print()