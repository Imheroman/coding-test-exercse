# https://www.acmicpc.net/problem/14620
# 꽃길
import sys

input = sys.stdin.readline

DIRECTIONS = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]

N = int(input())
graphs = [list(map(int, input().split())) for _ in range(N)]
# N = 6
# graphs = [
#     [1, 0, 2, 3, 3, 4],
#     [1, 1, 1, 1, 1, 1],
#     [0, 0, 1, 1, 1, 1],
#     [3, 9, 9, 0, 1, 99],
#     [9, 11, 3, 1, 0, 3],
#     [12, 3, 0, 0, 0, 1]
# ]


def calculate_cost(graph, visited):
    global answer

    result = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                result += graph[i][j]
    answer = min(answer, result)


def is_possible(row, col, visited):
    for dx, dy in DIRECTIONS:
        r, c = row + dx, col + dy
        if not (0 <= r < N and 0 <= c < N and not visited[r][c]):
            return False
    return True


def back_tracking(graph, visited, size=3):
    if size == 0:
        calculate_cost(graph, visited)
        return

    for row in range(N):
        for col in range(N):
            if not visited[row][col]:
                if is_possible(row, col, visited):
                    for dx, dy in DIRECTIONS:
                        visited[row + dx][col + dy] = True
                    back_tracking(graph, visited, size - 1)
                    for dx, dy in DIRECTIONS:
                        visited[row + dx][col + dy] = False


v = [[False] * N for _ in range(N)]
answer = int(1e10)
back_tracking(graphs, v)
print(answer)