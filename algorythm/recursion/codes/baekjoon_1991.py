# https://www.acmicpc.net/problem/1991
# 트리 순회
import sys

input = sys.stdin.readline


def preorder(graph, current):
    print(current, end='')
    l, r = graph[current]

    if l != ".":
        preorder(graph, l)

    if r != ".":
        preorder(graph, r)


def inorder(graph, current):
    l, r = graph[current]

    if l != ".":
        inorder(graph, l)

    print(current, end='')

    if r != ".":
        inorder(graph, r)


def postorder(graph, current):
    l, r = graph[current]

    if l != ".":
        postorder(graph, l)

    if r != ".":
        postorder(graph, r)

    print(current, end='')


N = int(input())
graphs = {}

for _ in range(N):
    parent, left, right = input().rstrip().split()
    graphs[parent] = [left, right]
# N = 7
# graphs = {"A": ["B", "C"], "B": ["D", "."], "C": ["E", "F"],
#           "E": [".", "."], "F": [".", "G"], "D": [".", "."], "G": [".", "."]}

preorder(graphs, list(graphs.keys())[0])
print()
inorder(graphs, list(graphs.keys())[0])
print()
postorder(graphs, list(graphs.keys())[0])