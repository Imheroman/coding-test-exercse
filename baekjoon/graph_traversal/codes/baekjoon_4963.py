# https://www.acmicpc.net/problem/4963
# 섬의 개수
import sys
from collections import deque

input = sys.stdin.readline
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, 1), (1, -1), (-1, -1)]  # 대각선 포함
# PROBLEMS = [
#     list(map(int, "1 1".split())),
#     [list(map(int, "0".split()))],
#     list(map(int, "2 2".split())),
#     [list(map(int, "0 1".split())),
#     list(map(int, "1 0".split()))],
#     list(map(int, "3 2".split())),
#     [list(map(int, "1 1 1".split())),
#     list(map(int, "1 1 1".split()))],
#     list(map(int, "5 4".split())),
#     [list(map(int, "1 0 1 0 0".split())),
#     list(map(int, "1 0 0 0 0".split())),
#     list(map(int, "1 0 1 0 1".split())),
#     list(map(int, "1 0 0 1 0".split()))],
#     list(map(int, "5 4".split())),
#     [list(map(int, "1 1 1 0 1".split())),
#     list(map(int, "1 0 1 0 1".split())),
#     list(map(int, "1 0 1 0 1".split())),
#     list(map(int, "1 0 1 1 1".split()))],
#     list(map(int, "5 5".split())),
#     [list(map(int, "1 0 1 0 1".split())),
#     list(map(int, "0 0 0 0 0".split())),
#     list(map(int, "1 0 1 0 1".split())),
#     list(map(int, "0 0 0 0 0".split())),
#     list(map(int, "1 0 1 0 1".split()))],
#     list(map(int, "0 0".split()))
# ]


def bfs(graph, start):
    need_visited = deque([start])

    while need_visited:
        x, y = need_visited.popleft()
        for dx, dy in DIRECTIONS:
            row, col = x + dx, y + dy
            if (0 <= row < len(graph) and 0 <= col < len(graph[0])
                    and graph[row][col] == 1):
                graph[row][col] = 0
                need_visited.append((row, col))


while True:
    H, W = map(int, input().split())
    if W == 0 and H == 0:
        break
    graphs = [list(map(int, input().split())) for _ in range(W)]
    answer = 0
    for w in range(W):
        for h in range(H):
            if graphs[w][h] == 1:
                bfs(graphs, (w, h))
                answer += 1
    print(answer)
