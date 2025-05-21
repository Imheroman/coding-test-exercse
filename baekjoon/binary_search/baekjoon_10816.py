# https://www.acmicpc.net/problem/10816
# 숫자 카드 2
import sys

input = sys.stdin.readline


def custom_bisect_left(card_list, target):
    start, end = 0, len(card_list)-1

    while start <= end:
        mid = (start + end) // 2

        if card_list[mid] >= target:
            # 현재의 값과 target의 값이 같은 경우에도 end를 start로 땡김.
            # 따라서, left로 이동하기 때문에 lower를 구할 수 있는 거임
            end = mid - 1
        else:
            start = mid + 1

    return start


def custom_bisect_right(card_list, target):
    start, end = 0, len(card_list) - 1

    while start <= end:
        mid = (start + end) // 2

        if card_list[mid] > target:  # 현재의 값이 target의 값보다 다 큰 경우에만 end를 앞으로 당긴다.
            end = mid - 1
        else:
            # 만약, 현재의 값이 동일하거나 target의 값이 더 크면 start가 커짐
            # -> 따라서, 값이 같은 경우에는 Upper를 구할 수 있는 거임
            start = mid + 1

    return start


# N = int(input())
# exist_cards = sorted(list(map(int, input().split())))
# M = int(input())
# cards = list(map(int, input().split()))
N = 10
exist_cards = sorted(list(map(int, "6 3 2 10 10 10 -10 -10 7 3".split())))
M = 8
cards = list(map(int, "10 9 -5 2 3 4 5 -10".split()))

for card in cards:
    left, right = custom_bisect_left(exist_cards, card), custom_bisect_right(exist_cards, card)
    # print("left:", left, "right:", right)
    print(right - left, end=' ')
