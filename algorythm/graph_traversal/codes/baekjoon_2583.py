# https://www.acmicpc.net/problem/2583
# 영역 구하기
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

M, N, K = map(int, input().split())
graphs = [[0] * N for _ in range(M)]


def dfs(graph, index):
    x, y = index
    count = 1

    graph[x][y] = 1
    for dx, dy in DIRECTIONS:
        r, c = x + dx, y + dy
        if 0 <= r < M and 0 <= c < N and graph[r][c] == 0:
            count += dfs(graph, (r, c))
    return count

answer = 0
for _ in range(K):
    lh, lw, rh, rw = list(map(int, input().split()))
    rw -= 1
    rh -= 1
    for row in range(lw, rw + 1):
        for col in range(lh, rh + 1):
            graphs[row][col] = -1

length_list = []
for i in range(M):
    for j in range(N):
        if graphs[i][j] == 0:
            answer += 1
            length_list.append(dfs(graphs, (i, j)))

print(answer)
print(*sorted(length_list), sep=" ")
