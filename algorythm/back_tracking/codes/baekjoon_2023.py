# https://www.acmicpc.net/problem/2023
# 신기한 소수
import math
import sys

input = sys.stdin.readline

ODD_NUMBERS = ['1', '3', '5', '7', '9']
PRIME_NUMBER = ['2', '3', '5', '7']

n = int(input())
answer = []


def is_prime_number(current):
    if current <= 1:  # 1보다 작은 수는 소수가 아님
        return False

    for divisor in range(2, int(math.sqrt(current)) + 1):  # 제곱근까지 수를 구함
        if current % divisor == 0:  # 현재수가 제곱근까지 나누어지는 수가 있으면, 소수가 아님
            return False
    return True


def generate_prime_number(number, size, result):
    if not is_prime_number(int(number)):
        return  # 소수가 아니면 그냥 끝냄

    if size == len(number):
        result.append(number)
        return

    for odd_number in ODD_NUMBERS:  # 홀수를 계속해서 더한다.
        generate_prime_number(number + odd_number, size, result)


for prime_number in PRIME_NUMBER:
    generate_prime_number(prime_number, n, answer)

for ans in answer:
    print(ans)