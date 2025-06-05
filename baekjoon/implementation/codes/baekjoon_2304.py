# https://www.acmicpc.net/problem/2304
# 창고 다각형
import sys

input = sys.stdin.readline

N = int(input())
graphs = [0 for _ in range(1001)]
max_height = 0
max_height_pos = -1

for _ in range(N):
    l, h = map(int, input().split())
    if h > max_height:
        max_height = h
        max_height_pos = l
    graphs[l] = h

left = 0
answer = max_height
for now in range(max_height_pos):
    left = max(graphs[now], left)
    answer += left

right = 0
for now in range(1000, max_height_pos, -1):
    right = max(graphs[now], right)
    answer += right

print(answer)