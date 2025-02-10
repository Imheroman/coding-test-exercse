# https://www.acmicpc.net/problem/2935
# 소음
from sys import stdin
input = stdin.readline

number1 = int(input())
op = input().rstrip()
number2 = int(input())

print(number1 + number2 if op == "+" else number1 * number2)
