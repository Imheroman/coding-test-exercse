# https://www.acmicpc.net/problem/1003
# 피보나치 수열

def solution(num, repository):
    for current in range(2, num + 1):
        index1 = current - 1
        index2 = current - 2

        repository[current][0] = repository[index1][0] + repository[index2][0]
        repository[current][1] = repository[index1][1] + repository[index2][1]


N = int(input())
DP = [{0: 0, 1: 0} for _ in range(41)]
DP[0] = {0: 1, 1: 0}
DP[1] = {0: 0, 1: 1}

for _ in range(N):
    number = int(input())
    solution(number, DP)
    print(DP[number][0], DP[number][1])
