# https://www.acmicpc.net/problem/11726
# 2*n 타일링

def solution(number, max_value, repository):
    for index in range(2, number + 1):
        repository[index] = (repository[index - 1] + repository[index - 2]) % max_value

    return repository[number]


MAX = 10_007
DP = [0] * 1_001
DP[0] = 1
DP[1] = 1
DP[2] = 2

N = int(input())
print(solution(N, MAX, DP))
