# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh
# View
T = 10
# T = 3

for problem in range(1, T + 1):
    N = int(input())
    buildings = list(map(int, input().split()))

    answer = 0
    for index in range(2, len(buildings) - 2):
        current = buildings[index]
        highest = max(buildings[index - 1], buildings[index - 2],
                      buildings[index + 1], buildings[index + 2])

        if current > highest:
            answer += current - highest  # 조망권을 구하기 위해 더 높은 곳의 길이를 뺌

    print(f"#{problem} {answer}")