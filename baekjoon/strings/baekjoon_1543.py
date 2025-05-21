# https://www.acmicpc.net/problem/1543
# 문서 검색
from sys import stdin
from collections import deque
input = stdin.readline

# 3
targets = input().rstrip("\n")
words = input().rstrip("\n")
answer = 0
index = 0

while index < len(targets):
    if targets[index:index + len(words)] == words:
        index += len(words)
        answer += 1
    else:
        index += 1

print(answer)

# 2
# queue = deque(input().rstrip("\n"))
# words = input().rstrip("\n")
# wordSize = len(words)
# answer = 0
#
# while queue and len(queue) >= wordSize:
#     for i in range(wordSize):
#         if queue[i] != words[i]:
#             queue.popleft()
#             break
#     else:
#         answer += 1
#         for i in range(wordSize):
#             queue.popleft()
#
# print(answer)

# 1
# targets = input().rstrip("\n")
# words = input().rstrip("\n")
# wordSize = len(words)
# answer = 0
# index = 0
#
# while index < len(targets):
#     if targets[index] == words[0]:
#         start = index
#         for i in range(wordSize):
#             if start < len(targets) and targets[start] == words[i]:
#                 start += 1
#             else:
#                 break
#         if start - index == wordSize:
#             index += wordSize - 1
#             answer += 1
#
#     index += 1
#
# print(answer)
