# https://www.acmicpc.net/problem/11727
# 2xN 타일링 2

def solution(dp, n):
    max_number = 10_007
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % max_number

    return dp[n]


DP = [1] * 1001
DP[2] = 3
N = int(input())
print(solution(DP, N))
