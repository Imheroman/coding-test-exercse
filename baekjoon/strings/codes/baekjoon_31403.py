# https://www.acmicpc.net/problem/31403
# $A + B - C$
from sys import stdin
input = stdin.readline

A = input().rstrip()
B = input().rstrip()
C = input().rstrip()

print(int(A) + int(B) - int(C))
print(int(A + B) - int(C))
