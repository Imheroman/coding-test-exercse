# https://www.acmicpc.net/problem/15666
# N과 M (12)
import sys

input = sys.stdin.readline


def combinations_with_replace(arr, start, size, repository=[]):
    # print("repository:", repository, ", size:", size)
    if size == 0:
        print(*repository, sep=' ')
        return

    for current in range(start, len(arr)):
        repository.append(arr[current])
        combinations_with_replace(arr, current, size - 1)
        repository.pop()


N, M = map(int, input().split())
number = sorted(set(map(int, input().split())))
# N, M = 3, 1
# number = sorted(set(map(int, "4 4 2".split())))
# N, M = 4, 2
# number = sorted(set(map(int, "9 7 9 1".split())))
# N, M = 4, 4
# number = sorted(set(map(int, "1 1 2 2".split())))

combinations_with_replace(number, 0, M)