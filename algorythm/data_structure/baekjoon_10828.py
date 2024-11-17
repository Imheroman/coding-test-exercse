# https://www.acmicpc.net/problem/10828
# 스택
# TODO: Here !
import sys


def solution(stack, command_dictionary, commands):
    if len(commands) == 2:
        stack.append(commands[1])
        return None

    operator = command_dictionary[commands[0]]
    return operator(stack)


N = int(sys.stdin.readline())
COMMAND_DICTIONARY = {
    "pop": lambda stack: stack.pop() if len(stack) > 0 else -1,
    "top": lambda stack: stack[-1] if len(stack) > 0 else -1,
    "size": lambda stack: len(stack),
    "empty": lambda stack: 1 if len(stack) == 0 else 0,
}
STACK = []

for _ in range(N):
    line = sys.stdin.readline()
    result = solution(STACK, COMMAND_DICTIONARY, line.split())

    if result is not None:
        print(result)
