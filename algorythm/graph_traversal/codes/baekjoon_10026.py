# https://www.acmicpc.net/problem/10026
# 적록색약
from sys import stdin
import sys
import copy

sys.setrecursionlimit(10 ** 6)
input = stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# N = int(input())
# graph = [list(input().rstrip()) for _ in range(N)]
N = 5
graph = [
    list("RGRBB"),
    list("GGBBB"),
    list("BBBRR"),
    list("BBRRR"),
    list("RRRRR")
]


def dfs(g, start, colors):
    x, y = start
    for dx, dy in DIRECTIONS:
        row, col = x + dx, y + dy
        if 0 <= row < N and 0 <= col < N and g[row][col] in colors:
            g[row][col] = "X"
            dfs(g, (row, col), colors)


answer = [0, 0]
deepcopy = copy.deepcopy(graph)
for r in range(N):
    for c in range(N):
        if graph[r][c] == "R" or graph[r][c] == "G":
            dfs(graph, (r, c), ["R", "G"])
            answer[1] += 1
        elif graph[r][c] == "B":
            dfs(graph, (r, c), ["B"])
            answer[1] += 1
        if deepcopy[r][c] == "R" or deepcopy[r][c] == "B" or deepcopy[r][c] == "G":
            dfs(deepcopy, (r, c), [deepcopy[r][c]])
            answer[0] += 1

print(*answer, sep=" ")
# print(graph)

