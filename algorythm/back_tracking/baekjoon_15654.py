
# https://www.acmicpc.net/problem/15654
# N과 M (5)
import sys

input = sys.stdin.readline


def permutations(arr, size, repository=[]):  # 1, 7, 8, 9
    # print(f"size: {size}, repository: {repository}")
    if size == 0:
        print(*repository, sep=' ')
        return

    elif 0 < size <= len(arr):
        for current in arr:
            if current not in repository:
                repository.append(current)
                permutations(arr, size - 1)
                repository.pop()


N, M = map(int, input().split())
permutation_matrix = sorted(list(map(int, input().split())))
# N, M = 3, 1
# permutation_matrix = sorted(list(map(int, "4 5 2".split())))
# N, M = 4, 2
# permutation_matrix = sorted(list(map(int, "9 8 7 1".split())))
# N, M = 4, 4
# permutation_matrix = sorted(list(map(int, "1231 1232 1233 1234".split())))

permutations(permutation_matrix, M)