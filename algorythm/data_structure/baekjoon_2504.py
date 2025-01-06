# https://www.acmicpc.net/problem/2504
# 괄호의 값
# 참고 블로그: https://velog.io/@rhdmstj17/백준-2504번-괄호의-값-python-stack-자세한-풀이
from sys import stdin
from collections import deque

input = stdin.readline

parentheses = list(input().rstrip())
# parentheses = list("[][]((])")
# parentheses = list("(()[[]])([])")
stack = deque()
parentheses_dict = {"(": 2, "[": 3}
answer = 0  # 정답을 관리하는 변수
direct = 1  # 계속해서 값을 누적하는 변수

for index in range(len(parentheses)):
    current = parentheses[index]  # 현재 문자
    if current == "(" or current == "[":  # 여는 괄호라면
        stack.append(current)  # 스택에 저장
        direct *= parentheses_dict[current]  # 분배의 법칙에 의해 현재의 값을 계속 곱함
    elif stack:  # stack 값이 있는 경우
        if ((current == ")" and parentheses[index - 1] == "(") or
                (current == "]" and parentheses[index - 1]) == "["):  # 처음 발견된 닫는 괄호일 때 값을 더함
            answer += direct
        if ((current == ")" and stack[-1] == "[")
                or (current == "]" and stack[-1] == "(")):  # # 괄호 조건이 맞지 않는 다면 break
            break
        direct //= parentheses_dict[stack.pop()]  # 닫는 괄호일 때 값을 2와 3으로 나눠줌으로써 괄호를 제거해 나감
    else:  # stack 값이 없는데 닫는 괄호가 나온 경우
        answer = 0
        break

if stack:
    answer = 0

print(answer)