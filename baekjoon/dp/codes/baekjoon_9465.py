# https://www.acmicpc.net/problem/9465
# 스티커
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    number = [list(map(int, input().split())) for _ in range(2)]

    repository = [[0] * n for _ in range(2)]

    repository[0][0], repository[1][0] = number[0][0], number[1][0]
    if n == 1:  # 1개일 때는, 현재까지 저장된 최댓값을 출력해주면 된다.
        print(max(repository[0][0], repository[1][0]))
        continue

    repository[0][1], repository[1][1] = (number[1][0] + number[0][1],
                                          number[0][0] + number[1][1])
    if n == 2:  # 2개일 때는, 최대한 많이 고르는 것이 좋기 때문에, 대각선으로 선택한 것이 최대인 것을 출력한다.
        print(max(repository[0][1], repository[1][1]))
        continue

    for current in range(2, n):  # 인덱스 1번까지(0, 1) 값을 구했기 때문에 2부터 시작한다
        # 현재 최댓값을 구하는 방법은 대각선으로 2번 오는 방법과, 2개 이전의 다리에서 대각선으로 현재 다리를 선택하는 방법이다.
        # 윗 다리와 아랫 다리의 최댓값이 다르기 때문에 2개로 저장을 해준다.
        repository[0][current] = max(repository[1][current - 1], repository[1][current - 2]) + number[0][current]
        repository[1][current] = max(repository[0][current - 1], repository[0][current - 2]) + number[1][current]

    print(max(repository[0][n - 1], repository[1][n - 1]))
