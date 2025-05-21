# https://www.acmicpc.net/problem/15829
# Hashing
from sys import stdin
input = stdin.readline

n = int(input())
alphabets = input().rstrip()
R, M = 31, 1234567891
result = 0

for index in range(len(alphabets)):
    alphabet = ord(alphabets[index]) - 96
    result += alphabet * (R ** index)

print(result % M)
