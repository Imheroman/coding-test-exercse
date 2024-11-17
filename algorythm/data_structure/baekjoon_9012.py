# https://www.acmicpc.net/problem/9012
# 괄호

def solution(parenthesis):
    stack = []

    for letter in parenthesis:
        if letter == "(":
            stack.append(letter)
        elif letter == ")":
            if stack:
                stack.pop()
            else:
                return "NO"

    return "YES" if len(stack) == 0 else "NO"


N = int(input())

for _ in range(N):
    line = input()
    print(solution(line))
