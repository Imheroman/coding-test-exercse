# https://www.acmicpc.net/problem/11403
# 경로 찾기
# 무슨 문제인지 1도 모르겠어서 블로그 보고 작성하면서 이해중
# 참고 블로그: https://great-park.tistory.com/20
import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = [[] for _ in range(N)]


def dfs(current, v):
    for n in range(N):
        if graph[current][n] == 1 and v[n] == 0:
            v[n] = 1
            dfs(n, v)


for i in range(N):
    visited = [0 for _ in range(N)]
    dfs(i, visited)
    print(*visited, sep=" ")
