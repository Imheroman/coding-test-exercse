# https://www.acmicpc.net/problem/1158
# 요세푸스 문제
import sys
from collections import deque


def solution(n, m, values):
    count = 0
    queue = deque(number for number in range(1, n+1))

    for value in values:
        length = len(queue)
        value_index = queue.index(value)

        if value != queue[0]:
            if length - value_index > value_index:
                while value != queue[0]:
                    left_value = queue.popleft()
                    queue.append(left_value)
                    count += 1
            else:
                while value != queue[0]:
                    right_value = queue.pop()
                    queue.appendleft(right_value)
                    count += 1

        queue.popleft()

    return count


N, M = map(int, sys.stdin.readline().split())
given_values = map(int, sys.stdin.readline().split())
print(solution(N, M, given_values))
