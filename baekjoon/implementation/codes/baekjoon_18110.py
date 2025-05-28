# https://www.acmicpc.net/problem/18110
# solved.ac
import sys
import math

input = sys.stdin.readline

TRIMMED_MEAN = 0.15

N = int(input())
ranks = sorted([int(input()) for _ in range(N)])
# N = 5
# ranks = [1, 5, 5, 7, 8]
# N = 10
# ranks = sorted([1, 13, 12, 15, 3, 16, 13, 12, 14, 15])
size = math.floor(N * TRIMMED_MEAN + 0.5)
result = ranks[size:N - size]

if len(result) == 0:
    print(0)
else:
    # print(sum(result) / len(result))
    # print(round(sum(result) / len(result)))
    print(math.floor((sum(result) / len(result)) + 0.5))
    # print(round(sum(result) / N))
