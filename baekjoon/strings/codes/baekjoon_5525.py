# https://www.acmicpc.net/problem/5525
# IOIOI
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

current = answer = count = 0
while current < M:
    if S[current: current + 3] == "IOI":
        print("if current:", current)
        count += 1
        current += 1
    else:
        count = 0

    if count == N:
        answer += 1
        count -= 1

    current += 1

print(answer)
