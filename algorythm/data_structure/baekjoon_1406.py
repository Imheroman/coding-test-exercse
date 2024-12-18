# https://www.acmicpc.net/problem/1406
# 에디터
import sys
"""
L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
P $	$라는 문자를 커서 왼쪽에 추가함
"""


def solution(l, r, m):
    for _ in range(m):
        commands = list(sys.stdin.readline().rstrip().split())
        print("l:", l, "-> r:", r, ", command:", commands[0])

        if commands[0] == "L" and l:
            r.append(l.pop())
        elif commands[0] == "D" and r:
            l.append(r.pop())
        elif commands[0] == "B" and l:
            l.pop()
        elif commands[0] == "P":
            l.append(commands[1])

    print("l:", l)
    print("r:", r)
    l.extend(reversed(r))

    return l


left = list(sys.stdin.readline().rstrip())
right = []
M = int(sys.stdin.readline())

print("".join(solution(left, right, M)))
