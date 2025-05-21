# https://www.acmicpc.net/problem/18429
# 근손실
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))


def back_tracking(n, kits, size, visited, result=0):
    global answer

    if result < 0:
        return

    if size == 0:
        answer += 1
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            back_tracking(n, kits, size - 1, visited, result + kits[i] - K)
            visited[i] = False


answer = 0
back_tracking(N, A, N, [False] * (N + 1))
print(answer)