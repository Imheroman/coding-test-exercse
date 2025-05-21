# https://www.acmicpc.net/problem/2805
# 나무 자르기

import sys

input = sys.stdin.readline

# N, M = map(int, input().split())  # N: 나무의 수, M: 나무의 길이
# trees = list(map(int, input().split()))
# N, M = 4, 7
# trees = [20, 15, 10, 17]
N, M = 5, 20
trees = [4, 42, 40, 26, 46]

start, end = 0, max(trees)
answer = 0
while start <= end:
    mid = (start + end) // 2
    total = 0

    for t in trees:
        if t > mid:
            total += t - mid
        if total >= M:
            break

    if total >= M:  # 더 적게 가져갈 수 있다면
        start = mid + 1
        answer = mid  # 일단 최솟값을 저장
    else:  # 기준 미달이라면 ? end 를 앞으로 당겨서 더 작은 수를 minus
        end = mid - 1

print(answer)
