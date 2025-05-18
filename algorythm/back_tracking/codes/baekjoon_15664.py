# https://www.acmicpc.net/problem/15664
# N과 M (10)
import sys

input = sys.stdin.readline


def combinations(arr, start, size, repository=[], answer=[]):
    if size == 0 and repository not in answer:
        answer.append(repository.copy())
        print(*repository, sep=' ')
        return

    for current in range(start, len(arr)):
        repository.append(arr[current])
        combinations(arr, current + 1, size - 1)
        repository.pop()


N, M = map(int, input().split())
number = sorted(list(map(int, input().split())))
# N, M = 3, 1
# number = sorted(list(map(int, "4 4 2".split())))
# N, M = 4, 2
# number = sorted(list(map(int, "9 7 9 1".split())))
# N, M = 4, 4
# number = sorted(list(map(int, "1 1 2 2".split())))

combinations(number, 0, M)