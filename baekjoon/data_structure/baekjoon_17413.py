# # https://www.acmicpc.net/problem/17413
# # 단어 뒤집기2
from sys import stdin
from collections import deque

input = stdin.readline

line = input().rstrip()
stack = deque()
tags = deque()
answer = deque()

for letter in line:
    print("letter:", letter)
    if letter == "<":
        tags.append(letter)
        while stack:
            answer.append(stack.pop())
    elif letter == ">":
        tags.append(letter)
        while tags:
            answer.append(tags.popleft())
    elif letter == " " and not tags:
        while stack:
            answer.append(stack.pop())
        answer.append(letter)
    elif tags:  # 태그가 진행중이면 태그에 저장
        tags.append(letter)
    else:  # 일반 문자열이면 stack에 저장
        stack.append(letter)

while stack:
    answer.append(stack.pop())

print(*answer, sep="")
