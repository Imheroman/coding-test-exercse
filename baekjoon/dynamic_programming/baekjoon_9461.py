# https://www.acmicpc.net/problem/9461
# 파도반 수열

def solution(dp, num):
    dp_size = len(dp)
    if dp_size >= num:
        return dp[num - 1]

    for index in range(dp_size, num):
        dp.append(dp[index - 5] + dp[index - 1])  # dp[index - 2] + dp[index - 3] 도 가능

    return dp[num - 1]


T = int(input())
N = [int(input()) for _ in range(T)]
# T = 2
# N = [6, 12]
DP = [1, 1, 1, 2, 2, 3, 4, 5]

for number in N:
    print(solution(DP, number))
