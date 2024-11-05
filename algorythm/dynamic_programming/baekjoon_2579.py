# https://www.acmicpc.net/problem/2579
# 계단 오르기

def solution(n, repository, supplier):
    if n == 1:  # 1이면 그냥 첫 계단까지
        return supplier[0]
    elif n == 2:  # 2이면 두번째 계단까지 더한 값
        return sum(supplier[:2])

    repository[0] = supplier[0]
    repository[1] = sum(supplier[:2])
    repository[2] = max(sum(supplier[1:3]),
                        supplier[0] + supplier[2])  # 3이면 그대로 3개를 올라갔거나, 2 계단을 건너뛴 값

    for index in range(3, n):
        print("index:", index, "-> dp:", repository, end=" / ")
        # DP[i] = max(DP[i-2] + stairs[i], DP[i-3] + stairs[i-1] + stairs[i])
        one_step = repository[index - 3] + supplier[index] + supplier[index - 1]
        two_step = repository[index - 2] + supplier[index]

        print("one_step:", one_step, "two_step:", two_step)

        repository[index] = max(one_step, two_step)

    return repository[n - 1]


# N = 6
# stairs = [10, 20, 15, 25, 10, 20]
N = int(input())
stairs = [int(input()) for _ in range(N)]
DP = [0] * (N + 1)

print(solution(N, DP, stairs))
