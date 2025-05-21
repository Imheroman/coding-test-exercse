# https://www.acmicpc.net/problem/15650
# N과 M (2)
import sys

input = sys.stdin.readline


def combinations(start, n, size, repository=[]):
    if size == 0:
        print(*repository, sep=' ')

    for current in range(start, n + 1):
        if current not in repository:
            repository.append(current)
            combinations(current + 1, n, size - 1)
            repository.pop()


N, M = map(int, input().split())
# N, M = map(int, "4 2".split())
# N, M = map(int, "4 3".split())
# N, M = map(int, "4 4".split())

combinations(1, N, M)