# https://www.acmicpc.net/problem/1920
# 수 찾기

def solution(numbers, num):
    return 1 if number in numbers else 0


N = int(input())
input_numbers = set(map(int, input().split()))
M = int(input())
find_numbers = list(map(int, input().split()))

for number in find_numbers:
    print(solution(input_numbers, number))
