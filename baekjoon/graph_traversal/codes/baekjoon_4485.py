# https://www.acmicpc.net/problem/4485
# 녹색 옷 입은 얘가 젤다지 ?
import heapq
import sys

input = sys.stdin.readline
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
INF = int(1e10)

problem = 0
while True:
    problem += 1
    N = int(input())

    if N == 0:
        break

    graphs = [list(map(int, input().split())) for _ in range(N)]
    # visited = [[INF] * (N + 1) for _ in range(N + 1)]
    visited = [[INF] * N for _ in range(N)]
    visited[0][0] = graphs[0][0]
    q = []
    heapq.heappush(q, (graphs[0][0], 0, 0))

    while q:
        current_cost, x, y = heapq.heappop(q)

        if visited[x][y] < current_cost:
            continue

        for dx, dy in DIRECTIONS:
            row, col = x + dx, y + dy
            if 0 <= row < N and 0 <= col < N:
                cost = current_cost + graphs[row][col]
                if visited[row][col] > cost:
                    visited[row][col] = cost
                    heapq.heappush(q, (cost, row, col))

    print(f"Problem {problem}: {visited[N - 1][N - 1]}")