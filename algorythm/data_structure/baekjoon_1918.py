# https://www.acmicpc.net/problem/1918
# 후위 표기식
# 내가 푼 코드 아님 다시 살펴보기
# 참고 블로그: https://zerotay.tistory.com/362
# 참고 블로그: https://0m1n.tistory.com/108
from sys import stdin

input = stdin.readline

# expression = input().rstrip()
expression = "A*(B+C)"
stack = []
answer = []

for letter in expression:
    if letter == "(":  # )가 나오기 전 까지 대기가 필요하므로 바로 push
        stack.append(letter)
    elif letter == ")":  # (가 나올 때 까지 현재까지 저장된 연산자들을 모두 pop
        while stack and stack[-1] != "(":
            answer.append(stack.pop())  # "(가 입력되기 전 까지의 값 저장
        stack.pop()  # "("를 제거
    elif letter == "*" or letter == "/":  # +, - 보다 연산 우선 순위가 높으므로 바로 pop
        while stack and (stack[-1] == "*" or stack[-1] == "/"):
            answer.append(stack.pop())
        stack.append(letter)
    elif letter == "+" or letter == "-":  # 우선 순위가 가장 낮으므로 현재까지 stack 들어 있는 모든 연산자들을 출력 후 저장
        while stack and stack[-1] != "(":
            answer.append(stack.pop())
        stack.append(letter)
    else:  # 문자인 경우에는 바로 append
        answer.append(letter)

while stack:
    answer.append(stack.pop())

print(*answer, sep="")
