# https://www.acmicpc.net/problem/1389
# 케빈 베이컨의 6단계 법칙
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
friends = [[float("INF")] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    friend1, friend2 = map(int, input().split())
    friends[friend1][friend2], friends[friend2][friend1] = 1, 1  # 양쪽 방향에 모두 가중치 설정

for i in range(1, N + 1):  # 자신을 가는 것은 0으로 처리
    friends[i][i] = 0

for k in range(1, N + 1):  # 거쳐가는 경유 친구 인덱스 (경유 인덱스)
    for i in range(1, N + 1):  # 친구 1
        for j in range(1, N + 1):  # 친구 2
            friends[i][j] = min(friends[i][j], friends[i][k] + friends[k][j])  # 친구1에서 친구2를 바로 가는 것과 k 친구를 거쳐서 가는 것 중 어떤 것이 더 빠른가

answer = 0
current_max = float("INF")
for index in range(1, len(friends)):
    friend_sum = sum(friends[index][1:])  # 전체 경유하는 친구들의 수가 가장 작은 것 찾기
    if friend_sum < current_max:
        current_max = friend_sum
        answer = index

print(answer)
