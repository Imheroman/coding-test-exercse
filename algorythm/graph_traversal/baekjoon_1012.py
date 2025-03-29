# https://www.acmicpc.net/problem/1012
# 유기농 배추
# 참고한 블로그 -> https://dduniverse.tistory.com/entry/백준-1012-유기농-배추-파이썬-python
# RecursionError 에러가 발생해서 검색 후 블로그에서 setrecursionlimit 참고
import sys
from sys import stdin

input = stdin.readline
sys.setrecursionlimit(10**6)

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 이동할 수 있는 4방향


def dfs(g, r, c):
    for dx, dy in DIRECTIONS:  # 방향에 따른 이동
        x, y = r + dx, c + dy  # 현재의 방향에서 이동할 방향으로 위치 변경
        if 0 <= x < len(g) and 0 <= y < len(g[0]) and g[x][y] == 1:  # 경계선을 넘었는지 확인 및 현재 값이 유효한지 확인
            g[x][y] = 0
            dfs(g, x, y)


T = int(input())
answers = []
for _ in range(T):  # 테스트 케이스의 수에 대해
    M, N, K = map(int, input().split())  # 가로 길이, 세로 길이, 배추 수
    graphs = [[0] * N for _ in range(M)]  # 그래프 생성

    for _ in range(K):
        a, b = map(int, input().split())  # 배추가 심어진 좌표
        graphs[a][b] = 1  # 좌표에 대해 배추 심기

    bugs = 0  # 필요한 지렁이 수 지렁이 == answer
    for index in range(M * N):
        row, col = index // N, index % N  # 좌표 구하기
        if graphs[row][col] == 1:  # 배추가 심어진 장소라면
            dfs(graphs, row, col)  # dfs로 탐색
            bugs += 1  # 탐색 당 1마리의 지렁이가 필요함

    answers.append(bugs)  # 탐색이 끝나면 필요한 지렁이 수를 답변에 추가

for ans in answers:
    print(ans)
