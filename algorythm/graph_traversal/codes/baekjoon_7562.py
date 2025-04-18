# https://www.acmicpc.net/problem/7562
# 나이트의 이동
import sys
from collections import deque

input = sys.stdin.readline
DIRECTIONS = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]


def bfs(graph, start, length):
    need_visited = deque([start])

    while need_visited:
        x, y = need_visited.popleft()
        for dx, dy in DIRECTIONS:
            row, col = x + dx, y + dy
            if 0 <= row < length and 0 <= col < length and graph[row][col] == 0:
                need_visited.append((row, col))
                graph[row][col] = graph[x][y] + 1


T = int(input())

for _ in range(T):
    L = int(input())
    current_position = list(map(int, input().split()))
    destination = list(map(int, input().split()))
    graphs = [[0] * L for _ in range(L)]

    if current_position == destination:
        print(0)
    else:
        bfs(graphs, current_position, L)
        print(graphs[destination[0]][destination[1]])
        # print(graphs[destination[0] - 1][destination[1] - 1])
