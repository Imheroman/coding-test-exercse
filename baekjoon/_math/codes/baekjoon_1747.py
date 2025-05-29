# # https://www.acmicpc.net/problem/1747
# # 소수 & 팰린드롬
# import sys
# import math
#
# input = sys.stdin.readline
#
# MAX_SIZE = 1_000_000
#
# # N = int(input())
# N = 31
# is_prime_number = [True] * (MAX_SIZE * 2 + 1)
# is_prime_number[0], is_prime_number[1] = False, False
#
# for i in range(2, int(math.sqrt(MAX_SIZE * 2 + 1)) + 1):
#     if is_prime_number[i]:
#         for j in range(i * i, MAX_SIZE * 2, i):
#             is_prime_number[j] = False
#
# current = N
# for i in range(N, MAX_SIZE + 1):
#     if is_prime_number[current]:
#         number = list(str(current))
#
#         if str(number) == str(number[::-1]):
#             print(current)
#             break

import sys
import math

input = sys.stdin.readline

MAX_SIZE = 1_000_000

N = int(input())

for current in range(N, MAX_SIZE + 1):
    is_prime = True
    for divisor in range(2, int(math.sqrt(current)) + 1):
        if current % divisor == 0:
            is_prime = False
            break

    if is_prime and str(current) == str(current)[::-1]:
        print(current)
        break