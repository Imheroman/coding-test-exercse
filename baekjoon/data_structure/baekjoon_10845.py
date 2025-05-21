# https://www.acmicpc.net/problem/10845
# 큐
import sys


def solution(queue, commands):
    if len(commands) > 1:
        number = commands[-1]
        queue.append(number)
        return

    command = commands[0]
    print(resolve_command(queue, command))
    return


def resolve_command(queue, command):
    if command == "pop":
        return queue.pop(0) if is_present(queue) else -1
    elif command == "size":
        return len(queue)
    elif command == "empty":
        return 1 if not is_present(queue) else 0
    elif command == "front":
        return queue[0] if is_present(queue) else -1
    elif command == "back":
        return queue[-1] if is_present(queue) else -1


def is_present(queue):
    return len(queue) >= 1


N = int(input())
QUEUE = []

for _ in range(N):
    line = sys.stdin.readline().split()
    solution(QUEUE, line)
