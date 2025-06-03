# https://www.acmicpc.net/problem/14891
# 톱니바퀴
import sys
from collections import deque

input = sys.stdin.readline

N, E, W, S = 0, 2, 6, 1
WHEEL_NUMBER = 8
WHEEL_SIZE = 4

wheels = [deque(list(map(int, input().rstrip()))) for _ in range(WHEEL_SIZE)]
K = int(input())


def rotate_wheel(wheel, d):
    if d == 1:
        wheel.appendleft(wheel.pop())
    elif d == -1:
        wheel.append(wheel.popleft())

    return wheel


for _ in range(K):
    target, direction = map(int, input().split())
    target -= 1

    direction_list = [0] * WHEEL_SIZE
    visited = [False] * WHEEL_SIZE
    need_visited = deque([target])

    direction_list[target] = direction
    visited[target] = True

    while need_visited:
        now = need_visited.popleft()

        for move in [now - 1, now + 1]:
            if 0 <= move < WHEEL_SIZE and not visited[move]:
                visited[move] = True

                if ((move > now and wheels[now][E] != wheels[move][W]) or  # now - move
                        (now > move and wheels[now][W] != wheels[move][E])):  # move - now
                    direction_list[move] = direction_list[now] * -1

                need_visited.append(move)

    for current in range(WHEEL_SIZE):
        wheels[current] = rotate_wheel(wheels[current], direction_list[current])

answer = 0
for current in range(WHEEL_SIZE):
    if wheels[current][N] == S:
        answer += 2 ** current

print(answer)