# https://www.acmicpc.net/problem/1541
# 잃어버린 괄호
from sys import stdin
from collections import deque
input = stdin.readline

origin_expression = stdin.readline().rstrip()
expression = deque(origin_expression.split("-"))
numbers = deque()
answer = 0

for index, letters in enumerate(expression):
    current = sum(map(int, letters.split("+")))
    answer -= current

    if index == 0 and origin_expression[0] != '-':
        answer *= -1

print(answer)
