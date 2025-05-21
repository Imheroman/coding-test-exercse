# https://www.acmicpc.net/problem/1038
# 감소하는 수
import sys
import itertools

input = sys.stdin.readline

N = int(input())
# N = 18
# N = 0
# N = 1000000

answer = []
for digit in range(1, 11):  # 최대는 9876543210 총 10자리이기 때문에
    for combination in itertools.combinations(range(10), digit):
        num = ''.join(list(map(str, reversed(list(combination)))))
        decrement_number = reversed(list(combination))
        answer.append(int("".join(list(map(str, decrement_number)))))

print()
answer.sort()
if N > len(answer):
    print(-1)
else:
    print(answer[N])
