# https://www.acmicpc.net/problem/15665
# N과 M (11)
import sys

input = sys.stdin.readline


def permutations(arr, size, repository=[]):
    if size == 0:
        print(*repository, sep=' ')
        return

    for index, current in enumerate(arr):
        repository.append(current)
        permutations(arr, size - 1)
        repository.pop()


# N, M = map(int, input().split())
# number = sorted(list(map(int, input().split())))
# N, M = 3, 1
# number = sorted(list(map(int, "4 4 2".split())))
# N, M = 4, 2
# number = sorted(set(map(int, "9 7 9 1".split())))
N, M = 4, 4
number = sorted(set(map(int, "1 1 2 2".split())))

permutations(number, M)
# for permutation in itertools.product(set(number), repeat=M):
#     print(*permutation, sep=' ')