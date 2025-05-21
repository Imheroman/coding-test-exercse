# https://www.acmicpc.net/problem/11052
# 카드 구매하기
import sys

input = sys.stdin.readline

N = int(input())
prices = list(map(int, input().rstrip().split()))
# N = 4
# prices = [1, 5, 6, 7]
# N = 5
# prices = [10, 9, 8, 7, 6]
# N = 10
# prices = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
repository = [0] + prices.copy()

for current in range(1, N + 1):  # 현재 구하는 카드의 수
    for increment_index in range(1, current + 1):  # 1 ~ current 까지
        # 현재 prices의 인덱스 값을 1씩 증가시키고, repository(dp)의 인덱스 값을 1씩 감소시켜서
        # 최적화된 답을 도출해낸다.
        # 결국, 연속된 인덱스에서도 최댓값을 찾을 수 있음
        repository[current] = max(repository[current],
                                  repository[current - increment_index] + prices[increment_index - 1])

print(repository[N])

"""
12
1 1 6 8 11 1 1 1 1 1 1 1
"""