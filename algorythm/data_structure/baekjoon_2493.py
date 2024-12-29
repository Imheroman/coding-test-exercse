# https://www.acmicpc.net/problem/2493
# 탑
# 참고 블로그: https://velog.io/@boorook/Python-백준-2493-탑-문제-풀이
from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
towers = deque(map(int, input().rstrip().split()))
stack = deque()
answers = [0] * N

for current_index, current_value in enumerate(towers):
    while stack and stack[-1][1] <= current_value:
        stack.pop()  # 현재의 값이 더 크다면 앞의 값들은 삭제. -> 처음 만나는 탑이 뒤의 탑들을 받기 때문

    if stack:  # 나보다 큰 탑이 존재하면
        answers[current_index] = stack[-1][0]  # 가장 먼저 만나는 탑의 위치를 저장

    stack.append((current_index + 1, current_value))  # 현재의 값을 저장

print(*answers, sep=" ")
