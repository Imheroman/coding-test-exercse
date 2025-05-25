# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AV15QRX6APsCFAYD&categoryId=AV15QRX6APsCFAYD&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1
# 보급로
import heapq

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
INF = int(1e10)


def dijkstra(arr, n, start):
    x, y = start
    distances = [[INF] * (n + 1) for _ in range(n + 1)]
    distances[x][y] = 0

    q = []
    heapq.heappush(q, (0, start))
    while q:
        current_cost, now = heapq.heappop(q)
        r, c = now

        if current_cost > distances[r][c]:
            continue

        for dx, dy in DIRECTIONS:
            row, col = r + dx, c + dy

            if not (0 <= row < n and 0 <= col < n):
                continue

            cost = current_cost + arr[row][col]
            if distances[row][col] > cost:
                distances[row][col] = cost
                heapq.heappush(q, (cost, (row, col)))

    return distances[n - 1][n - 1]


T = int(input())

for case in range(T):
    N = int(input())
    graphs = [list(map(int, input())) for _ in range(N)]
    print(f"#{case} {dijkstra(graphs, N, (0, 0))}")

"""

2
4
0100
1110
1011
1010
6
011001
010100
010011
101001
010101
111010

"""
