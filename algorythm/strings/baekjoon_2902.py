# https://www.acmicpc.net/problem/2902
# KMP는 왜 KMP일까 ?
from sys import stdin
input = stdin.readline

line = input().rstrip().split("-")
print(*map(lambda l: l[0], line), sep="")
