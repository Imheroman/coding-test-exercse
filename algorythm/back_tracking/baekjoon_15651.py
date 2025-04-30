# https://www.acmicpc.net/problem/15651
# N과 M (3)
import sys

input = sys.stdin.readline


def permutations(n, size, repository=[]):
    if size == 0:
        print(*repository, sep=' ')
        return

    for current in range(1, n + 1):
        repository.append(current)
        permutations(n, size - 1)
        repository.pop()


# N, M = map(int, input().split())
# N, M = map(int, "3 1".split())
N, M = map(int, "4 2".split())
# N, M = map(int, "4 3".split())
# N, M = map(int, "4 4".split())

permutations(N, M)