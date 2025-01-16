# https://www.acmicpc.net/problem/10824
# 네 수
from sys import stdin
input = stdin.readline

a, b, c, d = input().rstrip().split()
print(int(a + b) + int(c + d))
