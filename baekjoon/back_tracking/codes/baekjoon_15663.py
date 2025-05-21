# https://www.acmicpc.net/problem/15663
# N과 M (11)
import sys
import itertools

input = sys.stdin.readline


def permutations(arr, size, visited, repository=[]):
    if size == 0:
        print(*repository, sep=' ')
        return

    pre = -1
    for current in range(len(arr)):
        if arr[current] != pre and not visited[current]:
            pre = arr[current]
            visited[current] = True
            repository.append(arr[current])
            permutations(arr, size - 1, visited)
            visited[current] = False
            repository.pop()


# N, M = map(int, input().split())
# number = sorted(list(map(int, input().split())))
# N, M = 3, 1
# number = sorted(list(map(int, "4 4 2".split())))
N, M = 4, 2
number = sorted(list(map(int, "9 7 9 1".split())))
# N, M = 4, 4
# number = sorted(list(map(int, "1 1 1 1".split())))

v = [False] * N
permutations(number, M, v)