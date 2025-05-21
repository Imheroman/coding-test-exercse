# https://www.acmicpc.net/problem/15658
# 연산자 끼워넣기 (2)
import sys

input = sys.stdin.readline

MIN, MAX = 1, 0
ADD, SUB, MUL, DIV = 0, 1, 2, 3
OPERATE = {ADD: lambda x, y: x + y, SUB: lambda x, y: x - y,
           MUL: lambda x, y: x * y, DIV: lambda x, y: int(x / y)}

N = int(input())
number = list(map(int, input().split()))
operators = list(map(int, input().split()))
# N = 2
# number = [5, 6]
# operators = [1, 1, 1, 1]
# N = 3
# number = [3, 4, 5]
# operators = [2, 1, 2, 1]

answer = [int(-1e13), int(1e13)]


def backtracking(size, current, result):
    if size == len(number):
        answer[MAX] = max(answer[MAX], current)
        answer[MIN] = min(answer[MIN], current)
        return

    for index in range(4):
        if operators[index] > 0:
            operators[index] -= 1
            backtracking(size + 1, OPERATE[index](current, number[size]), result)
            operators[index] += 1


backtracking(1, number[0], answer)
print(*answer, sep='\n')