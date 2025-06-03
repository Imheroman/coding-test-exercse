# https://www.acmicpc.net/problem/9663
# N-Queen
# 참고 블로그: https://st-lab.tistory.com/118
import sys

input = sys.stdin.readline


def is_available(arr, row):
    print("arr:", arr)
    for r in range(row):
        print(f"row: {row}, r: {r} -> abs(row - r): {abs(row - r)} == abs(arr[row] - arr[r]): {abs(arr[row] - arr[r])}")
        if (arr[row] == arr[r]) or (abs(row - r) == abs(arr[row] - arr[r])):
            return False

    return True


def n_queen(arr, n, row):
    if row == n:
        global answer
        answer += 1
        # print("success arr:", arr)
        return

    for col in range(n):
        arr[row] = col

        if is_available(arr, row):
            n_queen(arr, n, row + 1)


# N = int(input())
N = 8
answer = 0
graphs = [0] * N
n_queen(graphs, N, 0)
print(answer)