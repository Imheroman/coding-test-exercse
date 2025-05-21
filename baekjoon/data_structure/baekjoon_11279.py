# https://www.acmicpc.net/problem/11279
# 최대 힙
import sys
import heapq


def solution(h, c):
    if c == 0:
        result = heapq.heappop(h) if h else 0
        print(result * -1)
    else:
        value = c * -1
        heapq.heappush(h, value)


N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    command = int(sys.stdin.readline())
    solution(heap, command)
