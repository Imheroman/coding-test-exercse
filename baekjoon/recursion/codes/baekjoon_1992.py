# https://www.acmicpc.net/problem/1992
# 쿼드트리
import sys

input = sys.stdin.readline
# 2중 배열을 count로 접근 -> 실패 => 총합으로 계산


def search(graph, size):
    result = sum([sum(g) for g in graph])

    if result == 0:
        print(0, end='')
    elif result == size ** 2:
        print(1, end='')
    else:
        print("(", end='')
        search([graph[row][:size//2] for row in range(size // 2)], size // 2)
        search([graph[row][size//2:] for row in range(size // 2)], size // 2)
        search([graph[row][:size//2:] for row in range(size // 2, len(graph))], size // 2)
        search([graph[row][size//2:] for row in range(size // 2, len(graph))], size // 2)
        print(")", end='')


N = int(input())
graphs = [list(map(int, list(input().rstrip()))) for _ in range(N)]
# N = 8
# graphs = [list(map(int, list("11110000"))), list(map(int, list("11110000"))), list(map(int, list("00011100"))), list(map(int, list("00011100"))), list(map(int, list("11110000"))), list(map(int, list("11110000"))),
#           list(map(int, list("11110011"))), list(map(int, list("11110011")))]

# print("graphs:", graphs)

search(graphs, N)

