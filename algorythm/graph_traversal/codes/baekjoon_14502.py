# https://www.acmicpc.net/problem/14502
# title
from collections import deque
from sys import stdin
import copy

input = stdin.readline

M, N = 7, 7
graphs = [
    list(map(int, "2 0 0 0 1 1 0".split())),
    list(map(int, "0 0 1 0 1 2 0".split())),
    list(map(int, "0 1 1 0 1 0 0".split())),
    list(map(int, "0 1 0 0 0 0 0".split())),
    list(map(int, "0 0 0 0 0 1 1".split())),
    list(map(int, "0 1 0 0 0 0 0".split())),
    list(map(int, "0 1 0 0 0 0 0".split()))
]
# M, N = map(int, input().rstrip().split())
# graphs = [list(map(int, input().rstrip().split())) for _ in range(M)]
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def virus(g, index):
    need_visited = deque([index])

    while need_visited:
        x, y = need_visited.popleft()

        for dx, dy in DIRECTIONS:
            row, col = x + dx, y + dy
            if 0 <= row < M and 0 <= col < N and g[row][col] == 0:
                need_visited.append((row, col))
                g[row][col] = 2


answer = 0

index_range = N * M
# for i in range(index_range):
for i in range(index_range // 2):
    copy_graph = copy.deepcopy(graphs)
    count = 0
    print("=" * 30, "i:", i, "=" * 30)
    if copy_graph[i // N][i % N] == 0:
        copy_graph[i // N][i % N] = 1
        count += 1
        print("i count")
    for j in range(i + 1, index_range, 1):
        if count == 1 and copy_graph[j // N][j % N] == 0:
            copy_graph[j // N][j % N] = 1
            count += 1
            print("j count")
        for k in range(j + 1, index_range, 1):
            if count == 2 and copy_graph[k // N][k % N] == 0:
                copy_graph[k // N][k % N] = 1
                count += 1
                print("k count")

            if count == 3:
                copy = copy_graph.copy()
                print("before bfs graph")
                for r in range(M):
                    for c in range(N):
                        if copy[r][c] == 2:
                            virus(copy, (r, c))
                print(copy_graph)
                print("after bfs graph")

                result = 0
                for c in copy:
                    print(c)
                    result += c.count(0)
                print(copy_graph)

                if result > answer:
                    print("if i:", i)
                    answer = result
                count = 2

print(answer)
