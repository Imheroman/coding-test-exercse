# https://www.acmicpc.net/problem/15657
# N과 M (8)
import sys

input = sys.stdin.readline


def combinations_with_replacement(arr, start, size, repository=[]):
    if size == 0:
        print(*repository, sep=' ')
        return

    for current in range(start, len(arr)):
        repository.append(arr[current])
        combinations_with_replacement(arr, current, size - 1)
        repository.pop()


# N, M = map(int, input().split())
# number = sorted(list(map(int, input().split())))
# N, M = 3, 1
# number = sorted(list(map(int, "4 5 2".split())))
N, M = 4, 2
number = sorted(list(map(int, "9 8 7 1".split())))
# N, M = 3, 3
# number = sorted(list(map(int, "1231 1232 1233".split())))

combinations_with_replacement(number, 0, M)
