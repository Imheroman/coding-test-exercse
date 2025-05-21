# # https://www.acmicpc.net/problem/1914
# # 하노이탑
# import sys
#
# input = sys.stdin.readline
#
#
# # def hanoi(n, departure, temp, destination):
# def hanoi(n, one, two, three):
#     if n == 1:
#         print(one, three)
#         return
#
#     hanoi(n - 1, one, three, two)
#     print(one, three)
#     hanoi(n - 1, two, one, three)
#
#
# def get_move_count(n):
#     return 2 ** n - 1  # 모든 원판 이동 횟수는 N^2 - 1의 값이 나온다.
#
#
# # N = int(input())
# N = 3
# print(get_move_count(N))
#
# if N <= 20:
#     hanoi(N, 1, 2, 3)

# https://www.acmicpc.net/problem/1914
# 하노이탑
import sys

input = sys.stdin.readline
SUM_TOTAL_TOWER_HEIGHT = 6


# def hanoi(n, departure, temp, destination):
def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return

    another_tower = SUM_TOTAL_TOWER_HEIGHT - start - end

    hanoi(n - 1, start, another_tower)
    print(start, end)
    hanoi(n - 1, another_tower, end)


def get_move_count(n):
    return 2 ** n - 1  # 모든 원판 이동 횟수는 N^2 - 1의 값이 나온다.


# N = int(input())
N = 3
print(get_move_count(N))

if N <= 20:
    hanoi(N, 1, 3)
