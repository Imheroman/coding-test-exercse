# https://www.acmicpc.net/problem/1717
# 집합의 표현
# 서로소 집합을 이용한 문제 해결. 서로소 집합 자료구조
from sys import stdin

input = stdin.readline

def find_parent(p, num):
    if p[num] != num:  # 만약 현재 노드에 저장된 값이 본래의 값이 아니면 == 부모 노드가 있음
        p[num] = find_parent(p, p[num])  # 부모 노드를 탐색, 압축 경로 테크닉을 이용

    return p[num]


def union_parent(p, a, b):
    a = find_parent(p, a)  # a의 루트 노드를 찾음
    b = find_parent(p, b)  # b의 루트 노드를 찾음

    if a > b:
        p[b] = a  # 더 큰 노드를 더 작은 노드로 연결
    else:
        p[a] = b


V, E = map(int, input().split())
parents = list(number for number in range(V + 1))

for _ in range(E):
    command, v1, v2 = map(int, stdin.readline().rstrip().split())

    if command == 0:  # 합집합
        union_parent(parents, v1, v2)
    else:  # 탐색
        if find_parent(parents, v1) == find_parent(parents, v2):
            print("YES")
        else:
            print("NO")
