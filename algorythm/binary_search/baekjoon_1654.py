# https://www.acmicpc.net/problem/1654
# 랜선 자르기
import sys

input = sys.stdin.readline

K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]
# K, N = 4, 11
# cables = [802, 743, 457, 539]

start, end = 1, max(cables)
answer = -1
while start <= end:
    mid = (start + end) // 2
    total = 0

    for c in cables:
        total += c // mid
        if total >= N:
            break

    if total >= N:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
