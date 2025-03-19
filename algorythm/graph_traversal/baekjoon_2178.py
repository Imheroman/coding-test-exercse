# https://www.acmicpc.net/problem/2178
# 미로 탐색
# 이것이 코딩테스트다 책 코드와 내용 확인 후 이해하여 코드 작성

from sys import stdin
from collections import deque

input = stdin.readline

DIRECTIONS = [(1, 0), (0, 1), (0, -1), (-1, 0)]
N, M = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]
need_visit = deque([(0, 0)])

while need_visit:
    x, y = need_visit.popleft()
    for dx, dy in DIRECTIONS:
        current_x, current_y = x + dx, y + dy

        if not (0 <= current_x < N and 0 <= current_y < M):
            continue

        if maze[current_x][current_y] == 1:
            need_visit.append([current_x, current_y])
            maze[current_x][current_y] = maze[x][y] + 1

print(maze[N - 1][M - 1])
