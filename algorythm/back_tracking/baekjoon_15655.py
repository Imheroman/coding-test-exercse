# https://www.acmicpc.net/problem/15655
# N과 M (6)
import sys

input = sys.stdin.readline


def combinations(arr, start, size, repository=[]):
    if size == 0:
        print(*repository, sep=' ')
        return

    for current in range(start, len(arr)):
        if arr[current] not in repository:
            repository.append(arr[current])
            combinations(arr, current + 1, size-1)
            repository.pop()


# N, M = map(int, input().split())
# number = sorted(list(map(int, input().split())))
# N, M = 3, 1
# number = sorted(list(map(int, "4 5 2".split())))
N, M = 4, 2
number = sorted(list(map(int, "9 8 7 1".split())))

combinations(number, 0, M)
