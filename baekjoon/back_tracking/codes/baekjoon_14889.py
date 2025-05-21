# https://www.acmicpc.net/problem/14889
# 스타트와 링크
import sys

input = sys.stdin.readline

N = int(input())
statistics = [list(map(int, (input().rstrip().split()))) for _ in range(N)]
# N = 4
# statistics = [
#     [0, 1, 2, 3],
#     [4, 0, 5, 6],
#     [7, 1, 0, 2],
#     [3, 4, 5, 0],
# ]

# N = 6
# statistics = [
#     [0, 1, 2, 3, 4, 5],
#     [1, 0, 2, 3, 4, 5],
#     [1, 2, 0, 3, 4, 5],
#     [1, 2, 3, 0, 4, 5],
#     [1, 2, 3, 4, 0, 5],
#     [1, 2, 3, 4, 5, 0],
# ]

# N = 8
# statistics = [
#     [0, 5, 4, 5, 4, 5, 4, 5],
#     [4, 0, 5, 1, 2, 3, 4, 5],
#     [9, 8, 0, 1, 2, 3, 1, 2],
#     [9, 9, 9, 0, 9, 9, 9, 9],
#     [1, 1, 1, 1, 0, 1, 1, 1],
#     [8, 7, 6, 5, 4, 0, 3, 2],
#     [9, 1, 9, 1, 9, 1, 0, 9],
#     [6, 5, 4, 3, 2, 1, 9, 0],
# ]


def backtracking(arr, start, size, visited):
    arr_size = len(arr)
    result = float('inf')

    if size == 0:
        start_team, link_team = 0, 0
        for i in range(arr_size):
            for j in range(arr_size):
                if i == j:  # i == j 인 경우는 모든 값이 0이긴 하지만, 그래도 continue 적용했음
                    continue

                if visited[i] and visited[j]:
                    start_team += arr[i][j]
                elif not visited[i] and not visited[j]:
                    link_team += arr[i][j]

        return min(result, abs(start_team - link_team))

    for current in range(start, arr_size):
        if not visited[current]:
            visited[current] = True
            result = min(result, backtracking(arr, current + 1, size - 1, visited))  # 조합이기 때문에 current + 1의 값을 넘겨준다.
            visited[current] = False

    return result


print(backtracking(statistics, 0, N // 2, [False] * (N + 1)))
