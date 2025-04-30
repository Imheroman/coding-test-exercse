# https://www.acmicpc.net/problem/15652
# N과 M (4)
import sys
import itertools

input = sys.stdin.readline


# N, M = map(int, input().split())
# N, M = map(int, "3 1".split())
# N, M = map(int, "4 2".split())
N, M = map(int, "3 3".split())
number = [number for number in range(1, N + 1)]

for combination in itertools.combinations_with_replacement(number,  M):
    print(*combination, sep=' ')
