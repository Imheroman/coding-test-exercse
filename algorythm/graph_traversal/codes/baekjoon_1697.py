# https://www.acmicpc.net/problem/1697
# 숨바꼭질
# TODO: Here!

from sys import stdin

MAX_SIZE = 100_002

input = stdin.readline

N, K = map(int, input().split())
repository = [float("INF")] * MAX_SIZE

if N >= K:
    print(N - K)
    exit()

for index in range(K + 1):
    repository[index] = abs(index - N)

for index in range(N + 1, K + 1):
    if index % 2 == 0:  # 짝수인 경우
        # index가 2로 나누어지기 때문에 바로 //2를 사용
        repository[index] = min(repository[index - 1] + 1, repository[index // 2] + 1)
    else:  # 홀수인 경우
        # index가 2로 나누어지지 않기 때문에 다음 숫자로 이동 후 이동
        # 따라서 2개를 더함
        repository[index] = min(repository[index - 1] + 1, repository[(index + 1) // 2] + 2)

print(repository[K])