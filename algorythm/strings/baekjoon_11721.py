# 열 개씩 끊어 출력하기
# https://www.acmicpc.net/problem/11721
# 참고 블로그: https://my-coding-notes.tistory.com/141

# 1
from sys import stdin

line = stdin.read()
print(line)


# 2
# line = stdin.read()
# print(line)
#
# while True:
#     try:
#         print(input())
#     except EOFError:
#         break