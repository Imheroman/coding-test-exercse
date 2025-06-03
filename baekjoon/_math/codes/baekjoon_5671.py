# https://www.acmicpc.net/problem/5671
# 호텔 방 번호
import sys

input = sys.stdin.readline

while True:
    line = input().rstrip()

    if line == "":
        break

    N, M = map(int, line.split())
    answer = 0
    for current in range(N, M + 1):
        if len(str(current)) == len(set(str(current))):
            answer += 1

    print(answer)