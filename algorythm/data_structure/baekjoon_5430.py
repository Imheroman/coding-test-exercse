# https://www.acmicpc.net/problem/5430
# AC
import sys
from collections import deque


def solution(command_list, number_list):
    is_reversed = False

    for command in command_list:
        if command == "R":
            is_reversed = not is_reversed
        elif command == "D" and number_list:
            if is_reversed:
                number_list.pop()
            else:
                number_list.popleft()
        else:
            return "error"

    if is_reversed:
        number_list.reverse()

    return "["+",".join(map(str, number_list))+"]"


T = int(sys.stdin.readline())

for _ in range(T):
    commands = sys.stdin.readline().rstrip()
    N = int(input())
    nums = eval(sys.stdin.readline().rstrip())
    numbers = deque(nums) if N > 0 else deque()

    print(solution(commands, numbers))
