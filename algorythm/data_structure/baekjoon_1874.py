# https://www.acmicpc.net/problem/1874
# 스택 수열
import sys


def solution(n, seq):
    current = 1
    res = []
    stack = []

    for current_sequence in seq:  # 1 2 5 3 4
        while current <= current_sequence and current <= n:
            stack.append(current)
            res.append("+")
            current += 1

        stack_number = stack.pop()

        if stack_number != current_sequence:
            return ["NO"]
        else:
            res.append("-")
    return res


N = int(sys.stdin.readline())
sequence = list(int(sys.stdin.readline()) for _ in range(N))
result = solution(N, sequence)

for answer in result:
    print(answer)
