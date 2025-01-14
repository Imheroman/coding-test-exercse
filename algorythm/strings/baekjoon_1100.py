# https://www.acmicpc.net/problem/1100
# 하얀 칸
from sys import stdin
input = stdin.readline

SIZE = 8
board = [list(input().rstrip()) for _ in range(SIZE)]
count = 0

for i in range(SIZE):
    for j in range(SIZE):
        if board[i][j] == "F":
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                count += 1

print(count)
