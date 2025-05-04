# https://www.acmicpc.net/problem/15686
# 치킨 배달
import sys

input = sys.stdin.readline


def backtrack(house_list, chicken_list, start, size, visited, answer=float('inf')):
    # print(house_list)
    # print(chicken_list)
    # print("backtrack")
    if size == 0:
        # print("house list:", house_list)
        # print("chicken list:", chicken_list)
        result = 0
        for house in house_list:
            house_row, house_col = house
            total = float('inf')
            for index, chicken in enumerate(chicken_list):
                if visited[index]:
                    chicken_row, chicken_col = chicken
                    total = min(total, abs(house_row - chicken_row) + abs(house_col - chicken_col))

            result += total
        # print("result:", result)
        return min(answer, result)

    # for current in chicken_list:
    for current in range(start, len(chicken_list)):
        if not visited[current]:
            visited[current] = True
            answer = min(answer, backtrack(house_list, chicken_list, start + 1, size - 1, visited))
            visited[current] = False

    return answer



N, M = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(N)]
# N, M = 5, 3
# cities = [
#     [0, 0, 1, 0, 0],
#     [0, 0, 2, 0, 1],
#     [0, 1, 2, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 2],
# ]
# N, M = 5, 2
# cities = [
#     [0, 2, 0, 1, 0],
#     [1, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0],
#     [2, 0, 0, 1, 1],
#     [2, 2, 0, 1, 2],
# ]
# N, M = 5, 1
# cities = [
#     [1, 2, 0, 0, 0],
#     [1, 2, 0, 0, 0],
#     [1, 2, 0, 0, 0],
#     [1, 2, 0, 0, 0],
#     [1, 2, 0, 0, 0],
# ]
# N, M = 5, 1
# cities = [
#     [1, 2, 0, 2, 1],
#     [1, 2, 0, 2, 1],
#     [1, 2, 0, 2, 1],
#     [1, 2, 0, 2, 1],
#     [1, 2, 0, 2, 1],
# ]
houses = []
chickens = []

for row in range(N):
    line = cities[row]
    for column in range(N):
        if line[column] == 1:
            houses.append((row, column))
        elif line[column] == 2:
            chickens.append((row, column))

print(backtrack(houses, chickens, 0, M, [False] * len(chickens)))
# answer = float('inf')
# for index, combination in enumerate(itertools.combinations(chickens, M)):
#     total = 0
#     for house in houses:
#         result = float('inf')
#         house_row, house_col = house
#         for chicken in combination:
#             chicken_row, chicken_col = chicken
#             current = abs(chicken_row - house_row) + abs(chicken_col - house_col)
#             if result > current:
#                 result = current
#
#         total += result
#
#     if answer > total:
#         answer = total
#
# print(answer)
