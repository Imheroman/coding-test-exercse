# https://www.acmicpc.net/problem/1158
# 뱀
from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
K = int(stdin.readline().rstrip())
APPLE_POSITIONS = list([False for _ in range(N + 1)] for _ in range(N + 1))
COMMANDS = []
COMMAND_DICTIONARY = {"L": False, "D": True}
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
x, y = 0, 0
direction_index = 0
current_position = deque((x, y))
answer = 0

for _ in range(K):
    ROW, COLUMN = map(int, stdin.readline().rstrip().split())
    APPLE_POSITIONS[ROW - 1][COLUMN - 1] = True

L = int(stdin.readline().rstrip())

for _ in range(L):
    X, C = stdin.readline().rstrip().split()
    COMMANDS.append((int(X), COMMAND_DICTIONARY[C]))
x
while 0 <= x < N and 0 <= y < N:
    answer += 1

    if APPLE_POSITIONS[x][y]:
        APPLE_POSITIONS[x][y] = False
    else:
        current_position.popleft()

    for command in COMMANDS:
        if command[0] == answer - 1:
            direction_index = (direction_index + 1 if command[1] else direction_index - 1) % len(directions)
            if direction_index < 0:
                direction_index = len(directions) - 1

    # print("direction index:", direction_index)
    row, column = directions[direction_index]
    x += row
    y += column

    if (x, y) in current_position:
        # print("x=" + str(x) + ", y=" + str(y))
        # print("current_position=" + str(current_position))
        # print("break")
        break

    current_position.append((x, y))
    # print("x=" + str(x) + ", y=" + str(y), "APPLE_POSITIONS=", APPLE_POSITIONS[x][y])

print(answer)






# print("N:", N)
# print("K:", K)
# print("L:", L)
# for row in range(len(APPLE_POSITIONS)):
#     print("row:", row, "-> [", end=" ")
#     for col in range(len(APPLE_POSITIONS[row])):
#         print(APPLE_POSITIONS[row][col], end=" ")
#     print("]")
#
# print("SNAKE_POSITIONS:", SNAKE_POSITIONS)
