# https://www.acmicpc.net/problem/2744
# 대소문자 바꾸기
from sys import stdin
input = stdin.readline

alphabets = input().rstrip()
answer = []

for alphabet in alphabets:
    if alphabet.islower():
        answer.append(alphabet.upper())
    else:
        answer.append(alphabet.lower())

print(*answer, sep="")
