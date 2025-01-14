# https://www.acmicpc.net/problem/9093
# 단어 뒤집기
from sys import stdin
input = stdin.readline

# 블로그 참고 (84ms) / https://velog.io/@ny_/백준-9093번.-단어-뒤집기-파이썬
N = int(input())

for i in range(N):
    answer = []
    lines = input().rstrip().split(" ")

    for line in lines:
        answer.append(line[::-1])
    print(" ".join(answer))

# 120ms
# from sys import stdin
# input = stdin.readline
#
# N = int(input())
# answer = []
#
# for i in range(N):
#     lines = input().rstrip().split(" ")
#
#     for line in lines:
#         answer.append(line[::-1] + ' ')
#     answer.append("\n")
#
# print(*answer, sep="")

# --
# origin (496ms)
# from sys import stdin
# input = stdin.readline
#
# N = int(input())
# answer = []
#
# for i in range(N):
#     lines = input().rstrip().split(" ")
#
#     for line in lines:
#         for index in range(len(line) - 1, -1, -1):
#             answer.append(line[index])
#         answer.append(" ")
#     answer.append("\n")
#
# print(*answer, sep="")
