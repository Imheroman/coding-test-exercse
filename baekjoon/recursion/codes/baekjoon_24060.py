# https://www.acmicpc.net/problem/24060
# 알고리즘 수업 - 병합 정렬 1
import sys

input = sys.stdin.readline

# N, K = map(int, input().split())
# A = list(map(int, input().split()))
N, K = 5, 7
A = [4, 5, 1, 3, 2]


def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    result = []
    s, e = start, mid + 1

    while s <= mid and e <= end:
        if arr[s] <= arr[e]:
            result.append(arr[s])
            s += 1
        else:
            result.append(arr[e])
            e += 1

    while s <= mid:
        result.append(arr[s])
        s += 1

    while e <= end:
        result.append(arr[e])
        e += 1

    s = start
    t = 0

    global count
    while s <= end:
        arr[s] = result[t]
        count += 1

        if count == K:
            print(arr[s])
            exit()

        s, t = s + 1, t + 1


count = 0
merge_sort(A, 0, len(A) - 1)
print(-1)