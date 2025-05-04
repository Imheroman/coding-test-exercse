# https://www.acmicpc.net/problem/1182
# 부분 수열의 합
import sys

input = sys.stdin.readline


def combinations(arr, start, size, target, repository=[]):
    result = 0

    if size == 0:
        # print(*repository)
        if sum(repository) == target:
            result += 1
        return result

    for current in range(start, len(arr)):
        # if arr[current] not in repository:
        repository.append(arr[current])
        result += combinations(arr, current + 1, size - 1, target, repository)
        repository.pop()

    return result


N, S = map(int, input().split())
number = list(map(int, input().split()))
# N, S = 5, 0
# number = [-7, -3, -2, 5, 8]
# N, S = 15, -7  # 1203
# number = [6, -4, 1, 3, -8, 5, -4, -3, 7, -4, 9, -9, -3, -4, -4]
# N, S = 15, 17  # 328
# number = [9, -2, 2, -2, 1, -3, 5, -3, -4, 1, 0, -9, 0, 7, 1]
# N, S = 5, 0
# number = [0, 0, 0, 0, 0]

# 1203

answer = 0
for index in range(1, N + 1):
    answer += combinations(number, 0, index, S)

print(answer)
