# https://www.acmicpc.net/problem/2667
# 단지 번호 붙이기
# 참고 블로그: https://ji-gwang.tistory.com/294 / 로직은 이해가 됐으나, 구현 부분이 조금 부족했음
"""
1. 전체를 순회하다가
2. 1을 발견하면 모든 방향에 주위에 1이 있는지 파악
3. 방문할 곳을 모두 방문하고, 숫자를 count
4. count += 1하고, result에 결과를 추가
"""
from collections import deque
from sys import stdin

input = stdin.readline
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(graph_list, r, c):
    graph_list[r][c] = 0
    result = 1
    for dx, dy in DIRECTIONS:
        x, y = r + dx, c + dy
        if 0 <= x < len(graph_list) and 0 <= y < len(graph_list[0]) and graph_list[x][y] == 1:
            graph_list[x][y] = 0
            result += dfs(graph_list, x, y)

    return result


answer = []
count = 0
N = int(input())
graphs = [list(map(int, input().rstrip())) for _ in range(N)]
need_visited = deque()

for current in range(N * N):
    row, col = current // N, current % N
    if graphs[row][col] == 1:
        answer.append(dfs(graphs, row, col))

print(len(answer))
for ans in sorted(answer):
    print(ans)

# BFS
# from collections import deque
# from sys import stdin
#
# input = stdin.readline
#
# DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# answer = []
# count = 0
# N = int(input())
# graphs = [list(map(int, input().rstrip())) for _ in range(N)]
# visited = [[False] * N for _ in range(N)]
# need_visited = deque()
#
# for current in range(N * N):
#     row, col = current // N, current % N
#     if graphs[row][col] == 0:
#         continue
#
#     need_visited.append((row, col))
#     graphs[row][col] = 0
#     count = 1
#
#     while need_visited:
#         r, c = need_visited.popleft()
#
#         for dx, dy in DIRECTIONS:
#             x, y = r + dx, c + dy
#             if 0 <= x < N and 0 <= y < N and graphs[x][y] == 1:  # check validation
#                 need_visited.append((x, y))
#                 graphs[x][y] = 0
#                 count += 1
#
#     answer.append(count)
#
# print(len(answer))
# for ans in sorted(answer):
#     print(ans)