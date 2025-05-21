# https://www.acmicpc.net/problem/1149
# RGB 거리

def insert_data(n, dp):
    for index in range(1, n + 1):
        r, g, b = map(int, input().split())
        dp[index][RED] = r
        dp[index][GREEN] = g
        dp[index][BLUE] = b


def solution(n, dp):
    for current in range(1, n + 1):
        for current_color in COLORS.keys():
            color_index1, color_index2 = COLORS[current_color]
            dp[current][current_color] += min(dp[current - 1][color_index1],
                                              dp[current - 1][color_index2])

    res = min(dp[n][RED], dp[n][GREEN], dp[n][BLUE]) # 3개의 마지막 색 중 가장 크기가 작은 것으로
    return res


RED = 0
GREEN = 1
BLUE = 2

COLORS = {
    RED: (GREEN, BLUE),
    GREEN: (RED, BLUE),
    BLUE: (GREEN, RED)
}

N = int(input())
DP = [[0, 0, 0] for _ in range(N + 1)]

insert_data(N, DP)
result = solution(N, DP)
print(result)
