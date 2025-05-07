# https://www.acmicpc.net/problem/1475
# 방 번호

import sys

input = sys.stdin.readline

numbers = list(map(int, input().rstrip()))
number_counts = {x: 0 for x in range(9)}

for number in numbers:
    if number == 9:
        number_counts[6] += 1
    else:
        number_counts[number] += 1

number_counts[6] = number_counts[6] // 2 + number_counts[6] % 2
print(max(number_counts.values()))