# https://www.acmicpc.net/problem/1927
# 최소힙
import sys
import heapq


def is_delete(com):
    return com == 0


def solution(h, com):
    if is_delete(com):
        result = heapq.heappop(h) if h else 0
        print(result)
        return

    heapq.heappush(h, com)


N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    command = int(sys.stdin.readline())
    solution(heap, command)
