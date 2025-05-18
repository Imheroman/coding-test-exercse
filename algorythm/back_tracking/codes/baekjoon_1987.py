# https://www.acmicpc.net/problem/1987
# 알파벳
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(graphs, direction, r, c, current, visited):
    global answer
    x, y = direction
    visited[graphs[x][y]] = True
    answer = max(answer, current)

    if answer == 26:
        return
    # print(visited)
    # result = current

    for dx, dy in DIRECTIONS:
        row, col = dx + x, dy + y

        if 0 <= row < r and 0 <= col < c and not visited[graphs[row][col]]:
            # current = max(dfs(graphs, (row, col), r, c, current + 1, visited), current)
            dfs(graphs, (row, col), r, c, current + 1, visited)
            visited[graphs[row][col]] = False

    # return current


R, C = map(int, input().split())
# boards = [list(input().rstrip()) for _ in range(R)]
boards = [list(map(lambda c: ord(c) - 65, input().strip())) for _ in range(R)]
# R, C = 2, 4
# boards = [
#     ["C", "A", "A", "B"],
#     ["A", "D", "C", "B"]
# ]
# R, C = 3, 6
# boards = [
#     list("HFDFFB"),
#     list("AJHGDH"),
#     list("DGAGEH"),
# ]

v = [False] * 26
# v = [number for number in range(26)]

answer = 0
dfs(boards, (0, 0), R, C, 1, v)
print(answer)
# print(dfs(boards, (0, 0), R, C, 1, v))
