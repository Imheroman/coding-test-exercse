# https://www.acmicpc.net/problem/16198
# 에너지 모으기
import sys

input = sys.stdin.readline

N = int(input())
number = list(map(int, input().split()))
# N = 4
# number = [1, 2, 3, 4]
# N = 5
# number = [100, 2, 1, 3, 100]


def back_tracking(arr, result):
    global answer

    if len(arr) == 2:  # 가운데를 뽑을 수 없을 때
        answer = max(answer, result)  # 기존에 있던 값과 계속 더해왔던 값의 최댓값을 구한다.
        return

    for i in range(1, len(arr) - 1):  # 양 옆의 구슬을 선택할 수 없으니, 1~전체 크기의 -1까지 탐색한다.
        current = result + arr[i - 1] * arr[i + 1]  # 현재 선택한 구슬의 업데이트된 값
        temp = arr.pop(i)  # 현재 구슬을 선택하였으니 제거한다.
        back_tracking(arr, current)  # 재귀로 반복
        arr.insert(i, temp)  # 모든 선택을 한 후에 다시 추가한다.


answer = 0
back_tracking(number, 0)
print(answer)