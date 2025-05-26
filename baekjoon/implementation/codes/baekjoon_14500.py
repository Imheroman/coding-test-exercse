# https://www.acmicpc.net/problem/14500
# 테트로미노
import sys

input = sys.stdin.readline
BLOCK_SIZE = 4
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N, M = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(N)]


# N, M = 5, 5
# graphs = [
#     [1, 2, 3, 4, 5],
#     [5, 4, 3, 2, 1],
#     [2, 3, 4, 5, 6],
#     [6, 5, 4, 3, 2],
#     [1, 2, 1, 2, 1]
# ]


def back_tracking(blocks, visited, start, current, size):
    if size == 0:
        return current

    result = 0
    for x, y in start:
        for dx, dy in DIRECTIONS:
            row, col = x + dx, y + dy
            if 0 <= row < N and 0 <= col < M and not visited[row][col]:
                visited[row][col] = True
                result = max(result, back_tracking(blocks, visited, start + [(row, col)], current + blocks[row][col], size - 1))
                visited[row][col] = False

    return result


v = [[False] * M for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(M):
        v[i][j] = True
        answer = max(answer, back_tracking(graphs, v, [(i, j)], graphs[i][j], BLOCK_SIZE - 1))

print(answer)