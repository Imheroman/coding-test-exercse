# https://www.acmicpc.net/problem/6588
# 골드바흐의 추측
import sys

input = sys.stdin.readline

MAX_NUMBER = 1_000_001

prime_numbers = [True] * MAX_NUMBER

for i in range(2, int(MAX_NUMBER ** 0.5) + 1):
    if prime_numbers[i]:
        for j in range(i * i, MAX_NUMBER, i):
            prime_numbers[j] = False

while True:
    number = int(input())

    if number == 0:
        break

    for i in range(3, number, 2):
        if prime_numbers[i] and prime_numbers[number - i]:
            print(f"{number} = {i} + {number - i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")