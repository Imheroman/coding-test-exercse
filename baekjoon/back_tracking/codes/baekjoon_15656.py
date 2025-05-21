# https://www.acmicpc.net/problem/15656
# N과 M (7)
import sys

input = sys.stdin.readline


def permutations(arr, size, repository=[]):
    if size == 0:
        print(*repository, sep=' ')
        return

    for current in arr:
        repository.append(current)
        permutations(arr, size - 1)
        repository.pop()


N, M = map(int, input().split())
number = sorted(list(map(int, input().split())))
# N, M = 3, 1
# number = sorted(list(map(int, "4 5 2".split())))
# N, M = 4, 2
# number = sorted(list(map(int, "9 8 7 1".split())))
# N, M = 3, 3
# number = sorted(list(map(int, "1231 1232 1233".split())))

permutations(number, M)
