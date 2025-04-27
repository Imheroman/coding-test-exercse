# https://www.acmicpc.net/problem/10819
# 차이를 최대로
import sys
from itertools import permutations

input = sys.stdin.readline

# N = int(input())
# A = list(map(int, input().split()))
N = 6
A = list(map(int, "20 1 15 8 4 10".split()))

answer = 0
for permutation in permutations(A):
    current_max = 0
    for i in range(1, N):
        current_max += abs(permutation[i - 1] - permutation[i])
    if current_max > answer:
        answer = current_max

print(answer)
