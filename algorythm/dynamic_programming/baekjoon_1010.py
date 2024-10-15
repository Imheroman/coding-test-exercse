# https://www.acmicpc.net/problem/1010
# 다리 놓기

import math

def factorial(num, dp):
    if dp[num] != 0:
        return dp[num]

    if num <= 1:
        return 1

    return num * factorial(num - 1, dp)


T = int(input())
DP = [0] * 31

for current in range(T):
    M, N = map(int, input().split())
    result = 1

    print(math.comb(N, M))
    # 조합 공식을 이용 nCr
    # if not (N == M or M == 0):  # (1)n과 r이 같거나 (2)r이 0일 경우 결과값은 1이다.
    #     nm = N - M
    #     DP[N] = factorial(N, DP)
    #     DP[M] = factorial(M, DP)
    #     DP[nm] = factorial(N - M, DP)
    # 
    #     result = (DP[N] // DP[M]) // DP[nm]
    # print(result)
