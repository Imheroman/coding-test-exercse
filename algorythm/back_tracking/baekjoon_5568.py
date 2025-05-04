# https://www.acmicpc.net/problem/5568
# 카드 놓기
import sys
import itertools


def permutations(arr, size, result, visited, repository=[]):
    if size == 0:
        value = ''.join(repository)
        if value not in result:
            result.add(value)
        return

    for index, num in enumerate(arr):
        # if num not in repository:
        if not visited[index]:
            visited[index] = True
            repository.append(num)
            permutations(arr, size - 1, result, visited)
            repository.pop()
            visited[index] = False


input = sys.stdin.readline
n = int(input())
k = int(input())
numbers = [input().rstrip() for _ in range(n)]
# n = 4
# k = 2
# numbers = sorted([1, 2, 12, 1])
# n = 6
# k = 3
# numbers = sorted(['1', '2', '2', '7', '12', '72'])

print(len(set("".join(val) for val in itertools.permutations(numbers, k))))