# https://www.acmicpc.net/problem/11053
# 가장 긴 증가하는 부분 수열
import sys

input = sys.stdin.readline


def solution(n, sequence, dp):
    for i in range(1, n):  # 2번째 인덱스부터 시작
        current_number = sequence[i]  # 현재 탐색중인 수
        for j in range(i):  # i번째 인덱스 전까지 순회 반복
            pre_sequence_number = sequence[j]  # 현재 탐색중인 수와 비교하기 위한 이전의 숫자들
            if current_number > pre_sequence_number:  # 현재 탐색중인 수가 더 크다면
                dp[i] = max(dp[i],  # 이전까지 진행된 수에서 현재 수를 더한 크기와,
                            dp[j] + 1)  # 현재 탐색중인 수의 크기를 비교하여 더 큰 수를 대입

    return max(dp)


# N = int(input())
# SEQUENCE = list(map(int, input().split()))
N = 5  # 부분 수열의 크기
# SEQUENCE = [10, 20, 10, 30, 20, 50]  # 부분 수열을 저장한 리스트
SEQUENCE = [3, 10, 2, 1, 201]
DP = [1] * (N + 1)  # 길이를 저장하는 DP

print(solution(N, SEQUENCE, DP))
