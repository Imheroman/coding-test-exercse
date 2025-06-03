# https://www.acmicpc.net/problem/1629
# 곱셈
import sys

input = sys.stdin.readline


def recursion(a, b, c):
    if b == 1:
        return a % c
    elif b == 0:
        return 1

    result = recursion(a, b // 2, c) % c
    result = result ** 2 % c
    if b % 2 == 1:
        result = result * a % c

    return result


A, B, C = map(int, input().split())
# A, B, C = 10, 11, 12
print(recursion(A, B, C))
