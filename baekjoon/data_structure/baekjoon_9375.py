# https://www.acmicpc.net/problem/9375
# 패션왕 신해빈
# 참고 사이트: https://hongcoding.tistory.com/60
from sys import stdin

input = stdin.readline

N = int(input())

for _ in range(N):
    answer = 1
    clothes_size = int(input())
    clothes = {}

    for _ in range(clothes_size):
        name, cloth_type = input().split()

        if cloth_type in clothes:
            clothes[cloth_type].append(name)
        else:
            clothes[cloth_type] = [name]

    for key in clothes:
        answer *= (len(clothes[key]) + 1)

    print(answer - 1)
