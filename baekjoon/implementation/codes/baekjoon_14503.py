# https://www.acmicpc.net/problem/14503
# 로봇 청소기
import sys

input = sys.stdin.readline

DIRECTIONS = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}  # 반시계방향

N, M = map(int, input().split())
row, col, direction = list(map(int, input().split()))  # (r, c) d(바라보는 방향)
spaces = [list(map(int, input().split())) for _ in range(N)]
# N, M = 3, 3
# row, col, direction = list(map(int, "1 1 0".split()))  # (r, c) d(바라보는 방향)
# spaces = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# N, M = 11, 10
# row, col, direction = list(map(int, "7 4 0".split()))  # (r, c) d(바라보는 방향)
# spaces = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
#     [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
#     [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]

answer = 1
spaces[row][col] = 2

while True:
    for _ in range(4):
        direction = (direction + 3) % 4
        x, y = DIRECTIONS[direction]
        if 0 <= row + x < N and 0 <= col + y < M and spaces[row + x][col + y] == 0:
            row, col = row + x, col + y
            spaces[row][col] = 2
            answer += 1
            break
    else:
        x, y = DIRECTIONS[(direction + 2) % 4]  # 후진 방향(총 4개의 방향에 동 <-> 서, 북 <-> 남으로 후진을 하기 때문에, +2를 하고 총 크기인 4로 나눠주면 된다.)
        row, col = row + x, col + y  # 후진
        if not (0 <= row < N and 0 <= col < M) or spaces[row][col] == 1:
            break

print(answer)
