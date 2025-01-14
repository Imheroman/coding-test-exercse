# https://www.acmicpc.net/problem/11656
# 접미사 배열
from sys import stdin
input = stdin.readline

# words = input().rstrip()
words = "baekjoon"
answer = []

for i in range(len(words)):
    answer.append(words[i:])

print(*sorted(answer), sep="\n")
