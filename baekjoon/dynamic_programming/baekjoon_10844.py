# https://www.acmicpc.net/problem/10844
# 쉬운 계단 수
# code: https://cotak.tistory.com/12


def solution(dp, n):
    for index in range(2, n + 1):
        dp[index][0] = dp[index - 1][1]
        dp[index][9] = dp[index - 1][8]

        for j in range(1, 9):
            dp[index][j] = (dp[index - 1][j - 1] + dp[index - 1][j + 1])

    return sum(dp[n]) % 1_000_000_000


N = int(input())
DP = list([0] * 10 for _ in range(N+1))

for i in range(1, 10):
    DP[1][i] = 1

print(solution(DP, N))