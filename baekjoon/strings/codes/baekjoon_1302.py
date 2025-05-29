# https://www.acmicpc.net/problem/1302
# 베스트 셀러
from sys import stdin
input = stdin.readline

# 정답 후 참고 블로그: https://woojinhong.tistory.com/97

N = int(input())
books = {}
answer = []

for _ in range(N):
    book = input().rstrip()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

max_value = max(books.values())

for key, value in books.items():
    if value == max_value:
        answer.append(key)

print(sorted(answer)[0])

# orogin
# ---
# from sys import stdin
# input = stdin.readline
#
# N = int(input())
# books = {}
# answer = ()
#
# for _ in range(N):
#     book = input().rstrip()
#     if book in books:
#         books[book] += 1
#     else:
#         books[book] = 1
#
# for key in books:
#     if not answer:
#         answer = (key, books[key])
#
#     if (answer[1] < books[key] or
#             (answer[1] == books[key] and answer[0] > key)):
#         answer = (key, books[key])
#
# print(answer[0])