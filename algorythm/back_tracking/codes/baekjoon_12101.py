# https://www.acmicpc.net/problem/12101
# 1, 2, 3 더하기 2
import sys
import itertools

input = sys.stdin.readline

NUMBERS = [1, 2, 3]

n, k = map(int, input().split())
# n, k = 4, 3
# n, k = 4, 5
# n, k = 4, 7
# n, k = 4, 8

answer = []
for digit in range(n, 0, -1):
    for combination in itertools.product(NUMBERS, repeat=digit):
        if sum(combination) == n:
            answer.append(combination)

if len(answer) < k:
    print(-1)
else:
    print(*sorted(answer)[k - 1], sep='+')
