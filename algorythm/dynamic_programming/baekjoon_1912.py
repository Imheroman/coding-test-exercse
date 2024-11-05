# https://www.acmicpc.net/problem/1912
# 연속합


def solution(numbers, n):
    dp = [0] * n  # arr[i]까지 고려했을 때 최대 연속합
    dp[0] = numbers[0]

    for i in range(1, n):
        dp[i] = max(numbers[i],
                    dp[i - 1] + numbers[i])  # arr[i] 혹은 이전 최대 연속합+arr[i]

    return max(dp)


N = int(input())
NUMBERS = list(map(int, input().split()))

print(solution(NUMBERS, N))
