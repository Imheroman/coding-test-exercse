# https://www.acmicpc.net/problem/10820
# 문자열 분석

LOWER_CASE = 0
UPPER_CASE = 1
NUMBER_CASE = 2
SPACE_CASE = 3

while True:
    answer = [0] * 4
    try:
        line = input()

        for letter in line:
            if letter.islower():
                answer[LOWER_CASE] += 1
            elif letter.isupper():
                answer[UPPER_CASE] += 1
            elif letter.isspace():
                answer[SPACE_CASE] += 1
            else:
                answer[NUMBER_CASE] += 1
        print(*answer)
    except EOFError:
        break
