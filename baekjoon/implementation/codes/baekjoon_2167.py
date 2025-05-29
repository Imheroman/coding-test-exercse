# https://www.acmicpc.net/problem/2167
# 2차원 배열의 합
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
number_list = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())
    answer = 0
    for row in range(i - 1, x):
        answer += sum(number_list[row][j - 1: y])
    print(answer)