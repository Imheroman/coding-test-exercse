# https://www.acmicpc.net/problem/2615
# 오목
import sys

input = sys.stdin.readline

BOARD_SIZE = 19
GOMOKU = 6
CUSTOM_DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

boards = [list(map(int, input().split())) for _ in range(BOARD_SIZE)]


def check(arr, start):
    x, y = start

    for dx, dy in CUSTOM_DIRECTIONS:
        row, col = x, y
        count = 0
        if 0 <= x - dx < BOARD_SIZE and 0 <= y - dy < BOARD_SIZE and arr[x][y] == arr[x - dx][y - dy]:
            continue
        for move in range(GOMOKU):
            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                if arr[x][y] == arr[row][col]:
                    count += 1
                else:
                    break
            row, col = row + dx, col + dy
        if count == 5:
            return True

    return False


for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
        if boards[j][i] == 0:
            continue

        if check(boards, (j, i)):
            print(boards[j][i])
            print(j + 1, i + 1)
            exit()

print(0)