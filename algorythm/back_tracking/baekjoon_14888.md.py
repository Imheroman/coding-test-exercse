# https://www.acmicpc.net/problem/14888
# 연산자 끼워넣기
#
import sys

input = sys.stdin.readline

ADD, SUB, MUL, DIV = 0, 1, 2, 3
OPERATE = {ADD: lambda x, y: x + y, SUB: lambda x, y: x - y,
           MUL: lambda x, y: x * y, DIV: lambda x, y: int(x / y)}


def permutations(nums, ops, idx, result, answer, count=0):
    count += 1
    if idx == len(nums):
        bigger, smaller = answer
        answer[0] = max(result, bigger)
        answer[1] = min(result, smaller)
        return

    if ops[ADD] > 0:
        ops[ADD] -= 1
        permutations(nums, ops, idx + 1, OPERATE[ADD](result, nums[idx]), answer)
        ops[ADD] += 1

    if ops[SUB] > 0:
        ops[SUB] -= 1
        permutations(nums, ops, idx + 1, OPERATE[SUB](result, nums[idx]), answer)
        ops[SUB] += 1

    if ops[MUL] > 0:
        ops[MUL] -= 1
        permutations(nums, ops, idx + 1, OPERATE[MUL](result, nums[idx]), answer)
        ops[MUL] += 1

    if ops[DIV] > 0:
        ops[DIV] -= 1
        permutations(nums, ops, idx + 1, OPERATE[DIV](result, nums[idx]), answer)
        ops[DIV] += 1


N = int(input())
operators = list(map(int, input().split()))
number = list(map(int, input().split()))

big = -10 ** 9
small = 10 ** 9

ans = [big, small]
permutations(number, operators, 1, number[0], ans)
print(ans[0], ans[1])
