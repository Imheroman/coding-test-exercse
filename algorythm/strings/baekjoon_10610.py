# https://www.acmicpc.net/problem/10610
# 30
# 참고 블로그: https://enlqn1010.tistory.com/51
from sys import stdin
input = stdin.readline

digits = sorted(input().rstrip(), reverse=True)
answer = -1

if sum(map(int, digits)) % 3 == 0 and digits[-1] == "0":
    answer = int("".join(digits))

print(answer)
