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

## origin

# # https://www.acmicpc.net/problem/1541
# # 잃어버린 괄호
# from sys import stdin
# from collections import deque
# input = stdin.readline
#
# expression = deque(stdin.readline())
# numbers = deque()
#
# while expression:
#     num = expression.popleft()
#
#     while expression and expression[0] != "-" and expression[0] != "+":
#         num += expression.popleft()
#
#     numbers.append(int(num))
#
# answer = 0
# stack = deque()
#
# while numbers:
#     if numbers[0] < 0:
#         answer += numbers.popleft()
#
#         while numbers and numbers[0] > 0:
#             answer -= numbers.popleft()
#     else:
#         answer += numbers.popleft()
# # for number in numbers:
# #     if number < 0:
# #         stack.append(-number)
# #     else:
# #         while stack:
# #             answer -= stack.pop()
# #         answer += number
#
# print(answer)
#
#
