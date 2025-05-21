# https://www.acmicpc.net/problem/18428
# 감시 피하기
import sys

input = sys.stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N = int(input())
graphs = []  # 전체 그래프
teachers = []  # 선생님 위치

for row in range(N):
    graphs.append(list(input().split()))
    for col in range(N):
        if graphs[row][col] == "T":
            teachers.append((row, col))


def is_possible(graph, current):  # 감시를 피할 수 있는가 ?
    for dx, dy in DIRECTIONS:  # 4가지 방향에 대해
        x, y = current

        while 0 <= x < N and 0 <= y < N:
            if graph[x][y] == "O":  # 만약 학생을 만나기 전에 장애물이 있다면 멈춤
                break

            if graph[x][y] == "S":  # 장애물을 만나기 전에 학생을 먼저 만나면 False
                return False

            x, y = x + dx, y + dy  # 이동 위치를 update 한다.
    return True


def back_tracking(graph, teacher_list, size):
    if size == 0:  # 장애물이 모두 설치됐을 때
        for teacher in teacher_list:  # 선생님의 위치를 탐색하여 학생을 만나는지 확인
            if not is_possible(graph, teacher):  # 만약 학생을 만나면
                return  # pass
        print("YES")  # 학생을 만나지 않고, 반복문이 끝나면 YES 후 프로그램이 종료된다.
        exit()

    for i in range(N):
        for j in range(N):
            if graph[i][j] == "X":  # 장애물을 설치할 수 있는 공간이면
                graph[i][j] = "O"  # 장애물 설치 후
                back_tracking(graph, teacher_list, size - 1)  # 재귀
                graph[i][j] = "X"  # 장애물을 다시 제거하여, 새로운 장애물을 만들 수 있도록 한다.


back_tracking(graphs, teachers, 3)
print("NO")  # YES가 출력되지 않았다면, NO가 출력된다.