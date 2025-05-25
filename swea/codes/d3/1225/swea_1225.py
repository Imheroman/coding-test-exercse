# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14uWl6AF0CFAYD
# 암호 생성기

from collections import deque

# T = 1
T = 10

for case in range(1, T + 1):
    N = int(input())
    arr = deque(list(map(int, input().split())))
    go = True
    current = 0
    while go:
        for i in range(1, 6):
            result = arr.popleft() - i
            if result <= 0:
                go = False
                arr.append(0)
                break
            arr.append(result)

    print(f"#{case}", end=' ')
    print(*list(arr))

"""

1
9550 9556 9550 9553 9558 9551 9551 9551
2
2419 2418 2423 2415 2422 2419 2420 2415

"""