# https://www.acmicpc.net/problem/1966
# 프린터 큐
import sys
from collections import deque


def set_track_index(importance_list, track, length):
    index = track - 1 if track > 0 else length - 1
    temp = importance_list.popleft()
    importance_list.append(temp)

    return index


def solution():
    order = 0
    size, track_index = list(map(int, sys.stdin.readline().split()))
    importance = deque(map(int, sys.stdin.readline().split()))

    for i in range(size):
        current_max_number = max(importance)

        while importance[0] != current_max_number:
            track_index = set_track_index(importance, track_index, len(importance))

        if importance[0] == current_max_number:
            order += 1
            if track_index == 0:
                break
            else:
                importance.popleft()
                track_index -= 1

    return order


N = int(sys.stdin.readline())

for _ in range(N):
    print(solution())
