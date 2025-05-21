# https://www.acmicpc.net/problem/10953
# A + B - 6
from sys import stdin
input = stdin.readline

N = int(input())

for _ in range(N):
    print(sum(map(int, input().split(","))))
