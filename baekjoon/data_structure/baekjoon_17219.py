# https://www.acmicpc.net/problem/17219
# 비밀번호 찾기
from sys import stdin

input = stdin.readline

N, M = map(int, input().rstrip().split())
passwords_dictionary = {}

for _ in range(N):
    url_path, password = input().rstrip().split()
    passwords_dictionary[url_path] = password

for _ in range(M):
    url_path = input().rstrip()
    print(passwords_dictionary[url_path])
