# https://www.acmicpc.net/problem/6603
# 로또
import sys


def combinations(arr, start, size, repository=[]):
    if size == 0:
        print(*repository)
        return

    for current in range(start, len(arr)):
        if arr[current] not in repository:
            repository.append(arr[current])
            combinations(arr, current + 1, size - 1)
            repository.pop()


input = sys.stdin.readline
LOTTO_SIZE = 6

while True:
    line = input().rstrip()

    if line == '0':
        break

    number = list(map(int, line.split()))
    k = number.pop(0)
    number.sort()

    combinations(number, 0, LOTTO_SIZE)
    # for combination in itertools.combinations(number, LOTTO_SIZE):
    #     print(*combination)
    print()