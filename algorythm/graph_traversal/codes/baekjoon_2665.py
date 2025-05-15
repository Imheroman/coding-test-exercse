# https://www.acmicpc.net/problem/2665
# 미로 만들기
import sys
from collections import deque

input = sys.stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N = int(input())
graphs = [list(map(int, list(input().rstrip()))) for _ in range(N)]
# N = 8
# graphs = [list(map(int, "11100110")), list(map(int, "11010010")), list(map(int, "10011010")),
#           list(map(int, "11101100")), list(map(int, "01000111")), list(map(int, "00110001")),
#           list(map(int, "11011000")), list(map(int, "11000111"))]


def bfs(graph):
    need_visited = deque([(0, 0)])
    visited = [[-1] * N for _ in range(N)]
    visited[0][0] = 0

    while need_visited:
        x, y = need_visited.popleft()

        if x == N - 1 and y == N - 1:
            break

        for dx, dy in DIRECTIONS:
            row, col = x + dx, y + dy

            if 0 <= row < N and 0 <= col < N and visited[row][col] == -1:  # 범위가 넘지 않고, 방문하지 않은 노드들에 대해 방문한다.
                if graph[row][col] == 1:  # 길이 이어져있다면 ?
                    need_visited.appendleft((row, col))  # 방문할 수 있는 길들을 이용하여 먼저 탐색하기 위해 appendleft
                    visited[row][col] = visited[x][y]  # 방문할 수 있는 길이기 때문에 따로 추가할 필요는 없다.
                else:  # 0이라면 ?
                    need_visited.append((row, col))  # 마지막에 탐색
                    visited[row][col] = visited[x][y] + 1  # 1을 1개 늘렸기 때문에, + 1

    print(visited[N - 1][N - 1])


bfs(graphs)