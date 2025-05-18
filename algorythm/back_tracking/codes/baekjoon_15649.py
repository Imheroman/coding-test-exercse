# https://www.acmicpc.net/problem/15649
# N과 M (1)
import sys

input = sys.stdin.readline


def permutations(n, size, repository=[]):
    if size == 0:
        print(*repository, sep=' ')
        return

    for current in range(1, n + 1):
        if current not in repository:
            repository.append(current)
            permutations(n, size - 1)
            repository.pop()


# N, M = map(int, input().split())
# N, M = map(int, "3 1".split())
N, M = map(int, "4 2".split())
permutations(N, M)
