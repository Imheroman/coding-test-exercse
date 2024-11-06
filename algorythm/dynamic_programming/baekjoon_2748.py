# https://www.acmicpc.net/problem/2748
# 피보나치 수2

def solution(n, dp):
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


N = int(input())
DP = [1] * 91

print(solution(N, DP))
