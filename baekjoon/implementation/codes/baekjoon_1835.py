# https://www.acmicpc.net/problem/1835
# 카드
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
answer = deque([])

for number in range(N, 0, -1):
    answer.appendleft(number)
    answer.rotate(number)

print(*answer)