# https://www.acmicpc.net/problem/7490
# 0 만들기
import sys

input = sys.stdin.readline

OPERATORS = [" ", "+", "-"]


def back_tracking(current, size, repository=["1"]):
    if size + 1 == current:
        result = "".join(repository)
        ans = result.replace(' ', '')
        if eval(ans) == 0:
            print(result)
        return

    for operator in OPERATORS:
        repository.append(operator + str(current))
        back_tracking(current + 1, size, repository)
        repository.pop()


T = int(input())
for _ in range(T):
    N = int(input())
    back_tracking(2, N)
    print()