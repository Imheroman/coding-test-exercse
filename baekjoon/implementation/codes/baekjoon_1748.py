# https://www.acmicpc.net/problem/1748
# 수 이어 쓰기2
import sys

input = sys.stdin.readline

N = int(input())
origin = N

answer = 0
for digit in range(1, len(str(N))):
    answer += digit * (9 * (10 ** (digit - 1)))

answer += (N - 10 ** (len(str(N)) - 1) + 1) * len(str(N))
# print(answer + (origin))
print(answer)
