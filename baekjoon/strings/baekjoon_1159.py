# https://www.acmicpc.net/problem/1159
# 농구 경기
from sys import stdin
input = stdin.readline

n = int(input())
dict = {}
answer = []

for index in range(ord('a'), ord('z') + 1):
    dict[chr(index)] = 0

for _ in range(n):
    name = input()
    dict[name[0]] += 1

for key, val in dict.items():
    if val >= 5:
        answer.append(key)

print(*answer if answer else "PREDAJA", sep="")
