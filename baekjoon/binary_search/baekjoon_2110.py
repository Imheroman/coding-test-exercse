# https://www.acmicpc.net/problem/2110
# 공유기 설치
# 참고 -> https://st-lab.tistory.com/277
import sys

input = sys.stdin.readline

# N, C = map(int, input().split())
# house_pos = sorted([int(input()) for _ in range(N)])
N, C = 5, 3
house_pos = sorted([1, 2, 8, 4, 9])

start, end = 0, N - 1

print(end)

