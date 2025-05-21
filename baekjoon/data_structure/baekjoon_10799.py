# https://www.acmicpc.net/problem/10799
# 쇠막대기
import sys


def solution(pipes):
    stack = 0
    count = 0
    i = 0

    while i < len(pipes):
        if pipes[i] == "(" and pipes[i + 1] == ")":
            count += stack
            i += 1
        else:
            if pipes[i] == "(":
                stack += 1
            else:
                stack -= 1
                count += 1

        i += 1

    return count


PIPES = list(sys.stdin.readline().strip())
print(solution(PIPES))
