# [1039번: 교환](https://www.acmicpc.net/problem/1039)

0으로 시작하지 않는 정수 N이 주어진다. 이때, M을 정수 N의 자릿수라고 했을 때, 다음과 같은 연산을 K번 수행한다.

> 1 ≤ i < j ≤ M인 i와 j를 고른다. 그 다음, i번 위치의 숫자와 j번 위치의 숫자를 바꾼다. 이때, 바꾼 수가 0으로 시작하면 안 된다.

위의 연산을 K번 했을 때, 나올 수 있는 수의 최댓값을 구하는 프로그램을 작성하시오.

## 입출력

### 입력
첫째 줄에 정수 N과 K가 주어진다. N은 1,000,000보다 작거나 같은 자연수이고, K는 10보다 작거나 같은 자연수이다.

### 출력
첫째 줄에 문제에 주어진 연산을 K번 했을 때, 만들 수 있는 가장 큰 수를 출력한다. 만약 연산을 K번 할 수 없으면 -1을 출력한다.

## 예제

### 예제 입력 1

```text
16375 1
```

### 예제 출력 1

```text
76315
```

### 예제 입력 2

```text
132 3
```

### 예제 출력 2

```text
312
```

### 예제 입력 3

```text
432 1
```

### 예제 출력 3

```text
423
```

### 예제 입력 4

```text
90 4
```

### 예제 출력 4

```text
-1
```


### 예제 입력 5

```text
5 2
```

### 예제 출력 5

```text
-1
```


### 예제 입력 6

```text
436659 2
```

### 예제 출력 6

```text
966354
```

## 알고리즘 분류

- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색

## 시도

SWEA의 D3 문제인 [최대 상금](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1) 문제를 풀다가 
백준에도 똑같은 문제가 있는 걸 알게 돼서 문제를 풀게 됐다.

처음에는, 어떻게 숫자를 교환해야 최댓수를 만들 수 있을지 고민하다가, 몇 번의 예제 실패로 인터넷에 검색을 하게 됐다. (현재는 늘 그렇듯 여러가지 정답이 있는 정답지를 외우기를 먼저 하려고 함)

[ConewLog](https://velog.io/@donew/%EB%B0%B1%EC%A4%80-1039%EA%B5%90%ED%99%98-Python)님의 블로그를 보게 되었고, BFS로 깔끔하게 문제를 해결한 걸 확인했다.

숫자 위치를 한 자리씩 다른 자리와 변경하면서, 변경한 횟수와 변경된 숫자를 저장하고, 지정한 카운트 수가 됐을 때 그 값을 비교하여 최댓값을 반환한다.   

### 시도1(34952kb, 88ms)

```python
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
```

## 정리

어느 정도 알고리즘 사용법은 알게 되었지만, 빠르게 성장하기 위해서 답을 많이 외우다보니 활용은 어려운 것 같다. 
