# https://www.acmicpc.net/problem/1932
# 정수 삼각형

N = int(input())  # 5
DP = [list(map(int, input().split())) for _ in range(N)]
# N = 5
# DP = [
#     [7],
#     [3, 8],
#     [8, 1, 0],
#     [2, 7, 4, 4],
#     [4, 5, 2, 6, 5]
# ]

for row in range(1, N):
    for col in range(row + 1):
        left = col - 1
        right = col

        if col == 0:  # 제일 좌측 열일때 (비교할 숫자가 없을 때)
            DP[row][col] += DP[row - 1][col]
        elif col == row:  # 제일 우측 열일때 (비교할 숫자가 없을 때)
            DP[row][col] += DP[row - 1][col - 1]
        else:  # 나머지 (비교할 숫자가 있을 때)
            DP[row][col] += max(DP[row - 1][left],
                                DP[row - 1][right])

print(max(DP[N - 1]))
