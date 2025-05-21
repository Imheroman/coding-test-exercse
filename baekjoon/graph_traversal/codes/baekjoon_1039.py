# https://www.acmicpc.net/problem/1039
# 교환
import sys
from collections import deque

input = sys.stdin.readline


def bfs(arr, size):
    answer = 0
    visited = set((0, arr))
    need_visited = deque([(0, arr)])

    while need_visited:
        c, now = need_visited.popleft()

        if c == size:
            answer = max(answer, now)
            continue

        now = list(str(now))
        for i in range(len(now) - 1):  # j는 i의 +1 이기 때문에 - 1을 진행
            for j in range(i + 1, len(now)):
                if i == 0 and now[j] == '0':  # 첫째 자리가 0인 걸 방지하기 위한 코드
                    continue

                now[i], now[j] = now[j], now[i]

                result = int("".join(now))
                if (c + 1, result) not in visited:
                    visited.add((c + 1, result))
                    need_visited.append((c + 1, result))

                now[i], now[j] = now[j], now[i]

    return answer



number, count = input().split()
# number, count = "381993", "3"
count = int(count)

res = bfs(int(number), count)

if res:
    print(res)
else:
    print(-1)
