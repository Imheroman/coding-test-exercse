# https://www.acmicpc.net/problem/7576
# 토마토
from collections import deque
from sys import stdin

input = stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N, M = map(int, input().split())  # 세로 수, 가로 수
graphs = [list(map(int, input().split())) for _ in range(M)]
need_visited = deque()

for index in range(M * N):
    row, col = index // N, index % N
    if graphs[row][col] == 1:
        need_visited.append((row, col))

while need_visited:
    row, col = need_visited.popleft()
    for dx, dy in DIRECTIONS:
        x, y = row + dx, col + dy
        if 0 <= x < M and 0 <= y < N and graphs[x][y] == 0:
                need_visited.append((x, y))
                graphs[x][y] = 1 + graphs[row][col]

answer = 0
for graph in graphs:
    for tomato in graph:
        if tomato == 0:
            print(-1)
            exit()
        if answer < tomato:
            answer = tomato

print(answer - 1)
