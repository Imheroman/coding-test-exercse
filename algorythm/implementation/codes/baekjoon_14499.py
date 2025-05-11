# https://www.acmicpc.net/problem/14499
# 주사위 굴리기
import sys

input = sys.stdin.readline

DIRECTIONS = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}


def turn(d, direction):
    north, middle, south, bottom, west, east = d
    if direction == 1:  # east
        return [north, west, south, east, bottom, middle]
    elif direction == 2:  # west
        return [north, east, south, west, middle, bottom]
    elif direction == 3:  # south
        return [bottom, north, middle, south, west, east]
    elif direction == 4:  # north
        return [middle, south, bottom, north, west, east]
    else:
        return


dice = [0, 0, 0, 0, 0, 0]  # north, middle, south, bottom, west, east
N, M, x, y, K = map(int, input().split())  # 지도 크기 N(row), M(col), 주사위 위치 x, y, 명령어 갯수 K
graphs = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))
# N, M, x, y, K = [4, 2, 0, 0, 8]
# graphs = [[0, 2], [3, 4], [5, 6], [7, 8]]
# commands = [4, 4, 4, 1, 3, 3, 3, 2]
# N, M, x, y, K = [3, 3, 1, 1, 9]
# graphs = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
# commands = [1, 3, 2, 2, 4, 4, 1, 1, 3]

for command in commands:
    r, c = DIRECTIONS[command]
    if not (0 <= x + r < N and 0 <= y + c < M):
        continue

    dice = turn(dice, command)
    x, y = x + r, y + c

    if graphs[x][y] == 0:
        graphs[x][y] = dice[3]
    else:
        dice[3] = graphs[x][y]
        graphs[x][y] = 0

    print(dice[1])
