# https://www.acmicpc.net/problem/1205
# 등수 구하기
import sys

input = sys.stdin.readline

N, score, P = map(int, input().split())
score_list = []

if N > 0:
    score_list = sorted(list(map(int, input().split())), reverse=True)

if N != 0 and score <= min(score_list) and N >= P:
    print(-1)
    exit()

answer = N + 1
for index in range(N):
    if score >= score_list[index]:
        answer = index + 1
        break
print(answer)