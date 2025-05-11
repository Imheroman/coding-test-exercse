# https://www.acmicpc.net/problem/14502
# # 연구소
from collections import deque
from sys import stdin

input = stdin.readline
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

M, N = map(int, input().rstrip().split())
graphs = [list(map(int, input().rstrip().split())) for _ in range(M)]
# M, N = 7, 7
# graphs = [
#     list(map(int, "2 0 0 0 1 1 0".split())),
#     list(map(int, "0 0 1 0 1 2 0".split())),
#     list(map(int, "0 1 1 0 1 0 0".split())),
#     list(map(int, "0 1 0 0 0 0 0".split())),
#     list(map(int, "0 0 0 0 0 1 1".split())),
#     list(map(int, "0 1 0 0 0 0 0".split())),
#     list(map(int, "0 1 0 0 0 0 0".split()))
# ]


def permutations(arr, size):
    answer = 0

    if size == 0:
        copy_graphs = [c[:] for c in arr]

        queue = deque()
        for i in range(M):
            for j in range(N):
                if copy_graphs[i][j] == 2:
                    queue.append((i, j))

        while queue:
            x, y = queue.popleft()

            for dx, dy in DIRECTIONS:
                row, col = x + dx, y + dy
                if 0 <= row < M and 0 <= col < N and copy_graphs[row][col] == 0:
                    queue.append((row, col))
                    copy_graphs[row][col] = 2

        return sum(graph.count(0) for graph in copy_graphs)

    for r in range(M):
        for c in range(N):
            if arr[r][c] == 0:
                arr[r][c] = 1
                answer = max(answer, permutations(arr, size - 1))
                arr[r][c] = 0

    return answer


print(permutations(graphs, 3))
