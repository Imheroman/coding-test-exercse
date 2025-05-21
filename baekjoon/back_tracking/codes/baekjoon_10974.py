# https://www.acmicpc.net/problem/10974
# 모든 순열
import sys

input = sys.stdin.readline


def permutations(arr, size, repository=[]):
    if size == 0:
        print(*repository)
        return

    for num in arr:
        if num not in repository:
            repository.append(num)
            permutations(arr, size - 1)
            repository.pop()


# N = int(input())
N = 3
number = [num for num in range(1, N + 1)]
permutations(number, N)