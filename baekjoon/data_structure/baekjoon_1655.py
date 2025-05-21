# https://www.acmicpc.net/problem/1655
# 가운데를 말해요
# 참고 사이트: https://velog.io/@junttang/BOJ-1655-가운데를-말해요-해결-전략-C, https://art-coding3.tistory.com/44
import heapq
from sys import stdin

input = stdin.readline

N = int(input())
max_heap = []
min_heap = []

for i in range(1, N + 1):
    number = int(input())

    if len(min_heap) >= len(max_heap):
        heapq.heappush(max_heap, (-number, number))
    else:
        heapq.heappush(min_heap, (number, number))

    if i > 1 and max_heap[0][1] > min_heap[0][1]:
        min_index, min_value = heapq.heappop(min_heap)
        max_index, max_value = heapq.heappop(max_heap)
        heapq.heappush(max_heap, (-min_index, min_value))
        heapq.heappush(min_heap, (-max_index, max_value))

    print(max_heap[0][1])




