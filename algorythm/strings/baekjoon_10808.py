# 알파벳 개수
# https://www.acmicpc.net/problem/10808
from sys import stdin
input = stdin.readline

# 1
# line = input().rstrip()
# alphabets = [0] * ALPHABET_NUMBERS
#
# for letter in line:
#     alphabets[ord(letter) % 97] += 1
#
# print(*alphabets, sep=" ")

# 2
# 더 빠름
ALPHABET_NUMBERS = 26
ALPHABET_ASCII_VALUE = 97
# line = input().rstrip()
line = "baekjoon"
alphabets = [0] * ALPHABET_NUMBERS

for i in range(ALPHABET_NUMBERS):
    alphabets[i] = line.count(chr(ALPHABET_ASCII_VALUE + i))

print(*alphabets, sep=" ")