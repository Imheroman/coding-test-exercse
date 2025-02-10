# https://www.acmicpc.net/problem/4999
# 아!
from sys import stdin
input = stdin.readline

me = input().rstrip()
doctor = input().rstrip()

print("no" if len(doctor) > len(me) else "go")
