# https://www.acmicpc.net/problem/11655
# ROT13
from sys import stdin
input = stdin.readline


def check_alphabet(condition, l):
    ascii_val = ord(l) + 13
    if not condition(chr(ascii_val)):
        ascii_val -= 26
    return chr(ascii_val)


lines = input()
answer = []

for letter in lines:
    if letter.isalpha():
        if letter.isupper():
            letter = check_alphabet(lambda let: "A" <= let <= "Z", letter)
        else:
            letter = check_alphabet(lambda let: "a" <= let <= "z", letter)
    answer.append(letter)

print(*answer, sep="")

# origin
# --
# from sys import stdin
# input = stdin.readline
#
#
# def check_alphabet(condition, l):
#     ascii_val = ord(l) + 13
#     if not condition(chr(ascii_val)):
#         ascii_val -= 26
#     return chr(ascii_val)
#
#
# # lines = input()
# lines = "Baekjoon Online Judge"
# answer = []
#
# for letter in lines:
#     if "a" <= letter <= "z" or "A" <= letter <= "Z":
#         letter = check_alphabet(lambda let: "a" <= let <= "z", letter)
#
#     elif "A" <= letter <= "Z":
#         letter = check_alphabet(lambda let: "A" <= let <= "Z", letter)
#     answer.append(letter)
#
# print(*answer, sep="")