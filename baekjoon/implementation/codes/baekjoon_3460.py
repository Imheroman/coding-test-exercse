# https://www.acmicpc.net/problem/3460
# 이진수
import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    answer = []
    current = int(input())

    while current > 0:
        answer.append(current % 2)
        current //= 2

    for index in range(len(answer)):
        if answer[index] == 1:
            print(index, end=' ')
