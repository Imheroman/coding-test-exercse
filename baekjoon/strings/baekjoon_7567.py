# https://www.acmicpc.net/problem/7567
# 그릇
from sys import stdin
input = stdin.readline

strings = input().rstrip()
height = 10

for index in range(1, len(strings)):
    if strings[index - 1] == strings[index]:
        height += 5
    else:
        height += 10

print(height)
