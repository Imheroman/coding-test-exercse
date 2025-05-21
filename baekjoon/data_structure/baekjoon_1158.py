# https://www.acmicpc.net/problem/1158
# 요세푸스 문제
import sys
from collections import deque


# queue 이용 방법
# def solution(n, k):
#     queue = deque([number for number in range(1, n + 1)])
#     answer = []
#
#     while queue:
#         for i in range(k):
#             pre = queue.popleft()
#             queue.append(pre)
#         answer.append(queue.pop())
#
#     return answer
def solution(n, k):
    sequence = list(number for number in range(1, n + 1))
    k -= 1
    current = k
    answer = []

    for sequence_length in range(n, 0, -1):
        if current >= sequence_length:
            current %= sequence_length

        answer.append(sequence.pop(current))
        current += k

    return answer


N, K = map(int, sys.stdin.readline().split())
result = solution(N, K)
print("<", ", ".join(map(str, result)), ">", sep="")
