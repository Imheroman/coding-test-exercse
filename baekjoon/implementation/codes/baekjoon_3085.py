import sys

input = sys.stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ROW = 0
COL = 1

N = int(input())
candies = [list(input().rstrip()) for _ in range(N)]


def back_tracking(arr, n, size):
    if size == 0:
        result = 0
        for i in range(n):
            count = [1, 1]
            for j in range(1, n):
                if arr[i][j] == arr[i][j - 1]:
                    count[ROW] += 1
                    result = max(count[ROW], result)
                if arr[i][j] != arr[i][j - 1]:
                    count[ROW] = 1

                if arr[j][i] == arr[j - 1][i]:
                    count[COL] += 1
                    result = max(count[COL], result)
                if arr[j][i] != arr[j - 1][i]:
                    count[COL] = 1

        return result

    answer = 0
    for nx in range(n):
        for ny in range(n):
            for dx, dy in DIRECTIONS:
                row, col = nx + dx, ny + dy
                if 0 <= row < n and 0 <= col < n and arr[nx][ny] != arr[row][col]:  # 현재 값과 인접한 값이 다른 값이면
                    arr[nx][ny], arr[row][col] = arr[row][col], arr[nx][ny]  # 교환
                    answer = max(answer, back_tracking(arr, n, size - 1))
                    arr[nx][ny], arr[row][col] = arr[row][col], arr[nx][ny]  # 재교환하여 원래 값으로 변경

    return answer


print(back_tracking(candies, N, 1))
