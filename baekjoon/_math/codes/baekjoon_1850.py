# https://www.acmicpc.net/problem/1850
# 최대 공약수
# 참고 블로그: https://claude-u.tistory.com/404
import sys

input = sys.stdin.readline


def uclid(smaller, bigger):
    if smaller == 0:
        return bigger

    return uclid(bigger % smaller, smaller)


# a, b = map(int, input().split())
a, b = 3, 6
# a = int("".join(map(str, [1] * a)))
# b = int("".join(map(str, [1] * b)))
print('1' * uclid(min(a, b), max(a, b)))