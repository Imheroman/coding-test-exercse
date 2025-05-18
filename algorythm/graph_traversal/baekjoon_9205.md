# [9205번: 맥주 마시면서 걸어가기](https://www.acmicpc.net/problem/9205)

송도에 사는 상근이와 친구들은 송도에서 열리는 펜타포트 락 페스티벌에 가려고 한다. 올해는 맥주를 마시면서 걸어가기로 했다. 출발은 상근이네 집에서 하고, 맥주 한 박스를 들고 출발한다. 맥주 한 박스에는 맥주가
20개 들어있다. 목이 마르면 안되기 때문에 50미터에 한 병씩 마시려고 한다. 즉, 50미터를 가려면 그 직전에 맥주 한 병을 마셔야 한다.

상근이의 집에서 페스티벌이 열리는 곳은 매우 먼 거리이다. 따라서, 맥주를 더 구매해야 할 수도 있다. 미리 인터넷으로 조사를 해보니 다행히도 맥주를 파는 편의점이 있다. 편의점에 들렸을 때, 빈 병은 버리고 새
맥주 병을 살 수 있다. 하지만, 박스에 들어있는 맥주는 20병을 넘을 수 없다. 편의점을 나선 직후에도 50미터를 가기 전에 맥주 한 병을 마셔야 한다.

편의점, 상근이네 집, 펜타포트 락 페스티벌의 좌표가 주어진다. 상근이와 친구들이 행복하게 페스티벌에 도착할 수 있는지 구하는 프로그램을 작성하시오.

## 입출력

### 입력

첫째 줄에 테스트 케이스의 개수 t가 주어진다. (t ≤ 50)

각 테스트 케이스의 첫째 줄에는 맥주를 파는 편의점의 개수 n이 주어진다. (0 ≤ n ≤ 100).

다음 n+2개 줄에는 상근이네 집, 편의점, 펜타포트 락 페스티벌 좌표가 주어진다. 각 좌표는 두 정수 x와 y로 이루어져 있다. (두 값 모두 미터, -32768 ≤ x, y ≤ 32767)

송도는 직사각형 모양으로 생긴 도시이다. 두 좌표 사이의 거리는 x 좌표의 차이 + y 좌표의 차이 이다. (맨해튼 거리)

### 출력

각 테스트 케이스에 대해서 상근이와 친구들이 행복하게 페스티벌에 갈 수 있으면 "happy", 중간에 맥주가 바닥나서 더 이동할 수 없으면 "sad"를 출력한다.

## 예제

### 예제 입력 1

```text
2
2
0 0
1000 0
1000 1000
2000 1000
2
0 0
1000 0
2000 1000
2000 2000
```

### 예제 출력 1

```text
happy
sad
```

## 알고리즘 분류

- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색

## 시도

### 시도1(34952kb, 56ms)

[마이노](https://velog.io/@stealmh/%EB%B0%B1%EC%A4%80-9205-%EB%A7%A5%EC%A3%BC-%EB%A7%88%EC%8B%9C%EB%A9%B4%EC%84%9C-%EA%B1%B8%EC%96%B4%EA%B0%80%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC)
님의 코드를 보고 작성한 코드이다.

가지고 있는 생명력(맥주)을 업데이트하면서, 목적지(페스티벌)까지 도착할 수 있는지를 구하는 문제이다.

일단 아래의 입력에서 편의점 개수, 상근이네 집, 편의점, 페스티벌 좌표가 주어진다고 했는데

```text
2
0 0
1000 0
1000 1000
2000 1000
```

왜 4개의 줄이 나오는지 이해가 안 되고, 배치가 어떻게 되는 건지 이해가 안 돼서 10분 정도 고민을 하다가 블로그를 검색해봤다.

문제 입력에 대해 이해한 후에 어떻게 풀어야할 지도 이해가 안 돼서 그냥 빨리 문제를 숙지하기 위해 일단 블로그를 보고 문제를 이해했다.

옛날에는 일단 나 혼자 푸는 것이 중요하다고 생각돼서 한 문제를 길게는 4시간 넘게도 잡고 있었던 적이 많았는데,
지금은 코딩테스트 시험을 준비하는 입장이라 빠르게 많은 유형을 풀고 싶어서 안 풀리면 일단 넘어가는 식으로 풀고 있다.

```python
# https://www.acmicpc.net/problem/9205
# 맥주 시면서 걸어가기
import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, store_list, destination):
    home_x, home_y = start
    visited = [False] * len(store_list)
    destination_x, destination_y = destination

    need_visited = deque([(home_x, home_y)])
    while need_visited:
        current_x, current_y = need_visited.popleft()

        if abs(current_x - destination_x) + abs(current_y - destination_y) <= 1000:  # 지금 20병을 가지고 목적지에 방문할 수 있으면 종료
            print("happy")
            return

        for i in range(len(store_list)):  # 전체 편의점 중
            if visited[i]:  # 방문했으면 pass
                continue

            store_x, store_y = store_list[i]  # 편의점 좌표
            move_x, move_y = abs(store_x - current_x), abs(store_y - current_y)  # 편의점을 이동할 수 있는 거리
            if move_x + move_y <= 1000:  # 편의점을 이동할 수 있으면 ?
                visited[i] = True  # 방문 처리
                need_visited.append((store_x, store_y))  # 편의점을 방문하는 기점으로 맥주가 업데이트 되니까 편의점의 좌표를 넣음

    print("sad")


t = int(input())
for _ in range(t):
    n = int(input())
    home = list(map(int, input().rstrip().split()))
    stores = [list(map(int, input().rstrip().split())) for _ in range(n)]
    festival = list(map(int, input().rstrip().split()))

    bfs(home, stores, festival)
```

## 정리

다양한 `bfs` 문제를 접해보는 게 좋을 것 같다.