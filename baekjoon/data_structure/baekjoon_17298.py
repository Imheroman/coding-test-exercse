# https://www.acmicpc.net/problem/17298
# 오큰수
from sys import stdin


def solution(nums, n):
    stack = []
    result = [-1] * n

    for current in range(n):
        while stack and nums[stack[LAST_INDEX]] < nums[current]:
            last_index = stack.pop()
            result[last_index] = nums[current]
        stack.append(current)

    return result


LAST_INDEX = -1
N = int(stdin.readline().rstrip())
numbers = list(map(int, stdin.readline().rstrip().split()))

print(*solution(numbers, N))

