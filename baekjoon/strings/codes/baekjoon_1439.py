# https://www.acmicpc.net/problem/1439
# 뒤집기

# 다른 사람 코드 가장 빠름 (32ms) / https://hazung.tistory.com/116
line = input().rstrip()
answer = 0

for i in range(1, len(line)):
    if line[i] != line[i-1]:
        answer += 1

print((answer + 1) // 2)

# --
# 혼자 수정해 본 것 (시간은 더 느림)
# from sys import stdin
# from collections import deque
# input = stdin.readline
#
# line = deque(input().rstrip())
# numbers = [line.popleft()]
#
# for number in line:
#     if numbers[-1] != number:
#         numbers.append(number)
#
# print(min(numbers.count("1"), numbers.count("0")))

# --
# origin
# from sys import stdin
# input = stdin.readline
#
# line = list(input().rstrip())
# zero_count = 0
# one_count = 0
#
# if line[0] == "1":
#     one_count += 1
# else:
#     zero_count += 1
#
# for i in range(1, len(line)):
#     if line[i] == '0' and line[i-1] == '1':
#         zero_count += 1
#     elif line[i] == '1' and line[i-1] == "0":
#         one_count += 1
#
# print(min(zero_count, one_count))
