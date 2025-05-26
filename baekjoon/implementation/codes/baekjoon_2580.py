# https://www.acmicpc.net/problem/2580
# 스도쿠
import sys

input = sys.stdin.readline

SUDOKU_BOARD_TOTAL_SIZE = 9
SUDOKU_BOARD_SIZE = 3


def is_valid_board(boards, current, n):
    x, y = current

    for index in range(SUDOKU_BOARD_TOTAL_SIZE):
        if boards[x][index] == n:
            return False
        if boards[index][y] == n:
            return False

    row_size = 3 * (x // SUDOKU_BOARD_SIZE)
    col_size = 3 * (y // SUDOKU_BOARD_SIZE)

    for row in range(row_size, row_size + SUDOKU_BOARD_SIZE):
        for col in range(col_size, col_size + SUDOKU_BOARD_SIZE):
            if boards[row][col] == n:
                return False
    return True


def back_tracking(boards, now, empty_list):
    if now == len(empty_list):
        for board in boards:
            print(*board)
        exit()

    for number in range(1, SUDOKU_BOARD_TOTAL_SIZE + 1):
        r, c = empty_list[now]
        if is_valid_board(boards, (r, c), number):
            boards[r][c] = number
            back_tracking(boards, now + 1, empty_list)
            boards[r][c] = 0

    return


graphs = []
empty = []
for i in range(SUDOKU_BOARD_TOTAL_SIZE):
    line = list(map(int, input().split()))
    graphs.append(line)
    for j in range(len(line)):
        if line[j] == 0:
            empty.append((i, j))

back_tracking(graphs, 0, empty)
