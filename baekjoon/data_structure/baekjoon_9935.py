# https://www.acmicpc.net/problem/9935
# 문자열 폭발
# 참고 사이트: https://edder773.tistory.com/26
from sys import stdin
from collections import deque

input = stdin.readline

strings = list(input().rstrip())
trigger = list(input().rstrip())
# strings = list("mirkovC4nizCC44")
# trigger = list("C4")
# strings = list("12ab112ab2ab")
# trigger = list("12ab")
answer = list()

trigger_size = len(trigger)
for letter in strings:
    answer.append(letter)

    if answer[-trigger_size:] == trigger:
        for _ in range(trigger_size):
            answer.pop()

print(*answer if answer else "FRULA", sep="")
