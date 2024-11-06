# https://www.acmicpc.net/problem/2156
# 포도주 시식
# TODO: here !

def solution(n, dp, wines):
    dp[0] = wines[0]
    if n > 1:
        dp[1] = wines[1] + wines[0]
    if n > 2:
        dp[2] = max(dp[1], wines[0] + wines[2], wines[1] + wines[2])

    for i in range(3, n):
        current = max(dp[i - 3] + wines[i - 1], dp[i - 2]) + wines[i]
        dp[i] = max(dp[i - 1], current)

    return dp[n - 1]


N = int(input())
WINES = list(int(input()) for _ in range(N))
DP = [0] * 10_001

print(solution(N, DP, WINES))
