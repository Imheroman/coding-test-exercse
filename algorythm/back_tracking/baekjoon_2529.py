# https://www.acmicpc.net/problem/2529
# 부등호
import sys
import itertools

input = sys.stdin.readline

K = int(input())
inequalities = list(input().split())
# K = 2
# inequalities = ["<", ">"]
# K = 9
# inequalities = [">", "<", "<", "<", ">", ">", ">", "<", "<"]
numbers = [x for x in range(10)]

answer = []
for permutation in itertools.permutations(numbers, K + 1):
    flag = True
    for current in range(len(inequalities)):
        num1, num2 = permutation[current], permutation[current + 1]
        inequality = inequalities[current]
        if inequality == ">":
            flag = num1 > num2
        else:
            flag = num1 < num2

        if not flag:
            break

    if flag:
        answer.append(permutation)

print(*max(answer), sep='')
print(*min(answer), sep='')