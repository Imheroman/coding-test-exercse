# https://www.acmicpc.net/problem/9205
# 맥주 시면서 걸어가기
import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, store_list, destination):
    home_x, home_y = start
    visited = [False] * len(store_list)
    destination_x, destination_y = destination

    need_visited = deque([(home_x, home_y)])
    while need_visited:
        current_x, current_y = need_visited.popleft()

        if abs(current_x - destination_x) + abs(current_y - destination_y) <= 1000:  # 지금 20병을 가지고 목적지에 방문할 수 있으면 종료
            print("happy")
            return

        for i in range(len(store_list)):  # 전체 편의점 중
            if visited[i]:  # 방문했으면 pass
                continue

            store_x, store_y = store_list[i]  # 편의점 좌표
            move_x, move_y = abs(store_x - current_x), abs(store_y - current_y)  # 편의점을 이동할 수 있는 거리
            if move_x + move_y <= 1000:  # 편의점을 이동할 수 있으면 ?
                visited[i] = True  # 방문 처리
                need_visited.append((store_x, store_y))  # 편의점을 방문하는 기점으로 맥주가 업데이트 되니까 편의점의 좌표를 넣음

    print("sad")


t = int(input())
for _ in range(t):
    n = int(input())
    home = list(map(int, input().rstrip().split()))
    stores = [list(map(int, input().rstrip().split())) for _ in range(n)]
    festival = list(map(int, input().rstrip().split()))

    bfs(home, stores, festival)
