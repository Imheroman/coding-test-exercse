# https://www.acmicpc.net/problem/1715
# 카드 정렬하기
# 참고 사이트: https://lazypazy.tistory.com/140
from sys import stdin
import heapq

input = stdin.readline

N = int(input())
cards = []
answer = 0

for _ in range(N):
    heapq.heappush(cards, int(input()))

while len(cards) > 1:
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)
    result = first + second
    answer += result
    heapq.heappush(cards, result)

print(answer)


