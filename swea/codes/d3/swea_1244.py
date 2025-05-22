# https://www.acmicpc.net/problem/1244
# 최대 상금
from collections import deque


def bfs(arr, size):
    answer = 0
    visited = []
    need_visited = deque([(0, arr)])

    while need_visited:
        c, now = need_visited.popleft()

        if c == size:
            answer = max(answer, int("".join(now)))
            continue

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                now[i], now[j] = now[j], now[i]

                result = int("".join(now))
                if (c + 1, result) not in visited:
                    visited.append((c + 1, result))
                    need_visited.append((c + 1, now[:]))

                now[i], now[j] = now[j], now[i]

    return answer


T = int(input())

for problem in range(1, T + 1):
    number, count = input().split()
    count = int(count)

    print(f"#{problem} {bfs(list(number), count)}")

"""
3
123 1
2737 1
32888 2

1
32888 2

1
432 1

1
123 1

"""