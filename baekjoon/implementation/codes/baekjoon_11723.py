# https://www.acmicpc.net/problem/11723
# 집합
import sys

input = sys.stdin.readline


M = int(input())
number = 0b0

for _ in range(M):
    line = input().split()
    operator = line[0]
    op = 0

    if len(line) == 2:
        op = int(line[1])

    bit_mask = 0b1 << op
    if operator == "add":
        number = number | bit_mask
    elif operator == "check":
        if number & bit_mask:
            print(1)
        else:
            print(0)
    elif operator == "remove":
        number = number & ~bit_mask
    elif operator == "toggle":
        repository[op] = not repository[op]
    elif operator == "all":
        repository = [True] * MAX_SIZE
    else:
        repository = [False] * MAX_SIZE