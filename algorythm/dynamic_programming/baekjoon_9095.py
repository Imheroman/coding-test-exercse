# 정수 n을 1, 2, 3을 이용하여 표현할 수 있는 방법

import sys
input = sys.stdin.readline


def solution(num, repository):
    for index in range(4, num + 1):
        if repository[index] == 0:
            repository[index] = repository[index-3] + repository[index-2] + repository[index-1]

    return repository[num]


N = int(input())
# numbers = [int(input()) for _ in range(N)]
# N = 3
# numbers = [4, 7, 10]

DP = [0] * 13
DP[0] = 0
DP[1] = 1
DP[2] = 2
DP[3] = 4

for _ in range(N):
    number = int(input())
    result = solution(number, DP)
    print(result)

