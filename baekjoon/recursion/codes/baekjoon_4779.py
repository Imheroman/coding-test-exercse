# https://www.acmicpc.net/problem/4779
# 칸토어 집합
import sys

input = sys.stdin.readline


def divide(arr, start, end):
    if end - start > 3:
        third = (end - start) // 3
        divide(arr, start, start + third)
        divide(arr, end - third, end)
    else:
        for current in range(start, end):
            if current % 2 == 0:
                arr[current] = "-"

    return arr


while True:
    line = input().rstrip()

    if line == "":
        break

    count = int(line)
    answer = [" " for _ in range(3 ** count)]
    print(*divide(answer, 0, 3 ** count), sep='')