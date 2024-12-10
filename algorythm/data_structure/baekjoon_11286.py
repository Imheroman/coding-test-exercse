# https://www.acmicpc.net/problem/11286
# 절댓값 힙
# TODO: Here !
import sys
import heapq


def solution(p_heap, n_heap, num):
    if num == 0:
        if p_heap or n_heap:
            if p_heap and not n_heap:
                print(heapq.heappop(p_heap))
            elif n_heap and not p_heap:
                print(heapq.heappop(n_heap) * - 1)
            else:
                if p_heap[0] >= n_heap[0]:
                    print(heapq.heappop(n_heap) * -1)
                else:
                    print(heapq.heappop(p_heap))
        else:
            print(0)
    else:
        if num < 0:
            heapq.heappush(n_heap, num * -1)
        else:
            heapq.heappush(p_heap, num)


N = int(sys.stdin.readline())
positive_heap = []
negative_heap = []

for _ in range(N):
    number = int(sys.stdin.readline())
    solution(positive_heap, negative_heap, number)
