# https://www.acmicpc.net/problem/4949
# 균형잡힌 세상
import sys


def solution(letters):
    stack = []
    result = "yes"

    for letter in letters:
        if letter == '[' or letter == '(':
            stack.append(letter)
        else:
            if letter == ']':
                if not stack or stack[-1] != "[":
                    result = "no"
                    break
                stack.pop()
            elif letter == ')':
                if not stack or stack[-1] != "(":
                    result = "no"
                    break
                stack.pop()

    return result if not stack else "no"


while True:
    line = sys.stdin.readline()
    print("line size:", len(line))

    if len(line) <= 2:
        if line.strip() == ".":
            break
    print(solution(line.strip()))