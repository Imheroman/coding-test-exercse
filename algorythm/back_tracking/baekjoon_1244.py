# https://www.acmicpc.net/problem/1244
# 스위치 켜고 끄기
import sys

input = sys.stdin.readline
MAN = 1

N = int(input())
switches = list(map(int, input().split()))
student_size = int(input())
# N = 8
# switches = [0, 1, 0, 1, 0, 0, 0, 1]
# student_size = 2
# students = [[1, 3], [2, 3]]

for _ in range(student_size):
    gender, index = list(map(int, input().split()))

    if gender == MAN:
        for current in range(index, N + 1, index):
            switches[current - 1] = int(not switches[current - 1])
    else:
        switches[index - 1] = int(not switches[index - 1])
        for current in range(1, N):
            left, right = index - current - 1, index + current - 1

            if (left < 0 or right >= N) or (switches[left] != switches[right]):
                break

            switches[left] = int(not switches[left])
            switches[right] = int(not switches[right])

for current in range(N):
    print(switches[current], end=' ')

    if (current + 1) % 20 == 0:
        print()

"""
0 0 1 1 1 1 0 1 1 1 1 
"""
"""
0 1 1 1 0 1 0 0 1 1 0 
"""