# 1654번: 랜선 자르기

집에서 시간을 보내던 오영식은 박성원의 부름을 받고 급히 달려왔다. 박성원이 캠프 때 쓸 N개의 랜선을 만들어야 하는데 너무 바빠서 영식이에게 도움을 청했다.

이미 오영식은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이다. 박성원은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다. 예를 들어
300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm는 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)

편의를 위해 랜선을 자르거나 만들 때 손실되는 길이는 없다고 가정하며, 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자. 그리고 자를 때는 항상 센티미터 단위로 정수길이만큼 자른다고
가정하자. N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.

## 입출력

### 입력

첫째 줄에는 오영식이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력된다. K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. 그리고 항상 K ≦ N
이다. 그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력된다. 랜선의 길이는 231-1보다 작거나 같은 자연수이다.

### 출력

첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.

## 예제

### 예제 입력 1

```text
4 11
802
743
457
539
```

### 예제 출력 1

```text
200
```

## 힌트

802cm 랜선에서 4개, 743cm 랜선에서 3개, 457cm 랜선에서 2개, 539cm 랜선에서 2개를 잘라내 모두 11개를 만들 수 있다.

## 알고리즘 분류

- 이분 탐색
- 매개 변수 탐색

## 시도

### 시도1

binary search 알고리즘 문제를 풀며 왔고, 문제에서 랜선의 길이는 2^31 - 1 보다 작거나 같은 자연수(2147483647) 이라고 했으므로 
binary search 를 이용하여 문제를 해결했지만, `ZeroDivisionError`가 발생했다.

```python
# https://www.acmicpc.net/problem/1654
# 랜선 자르기
import sys

input = sys.stdin.readline

K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]
# K, N = 4, 11
# cables = [802, 743, 457, 539]

start, end = 0, max(cables)
answer = -1
while start <= end:
    mid = (start + end) // 2
    total = 0

    for c in cables:
        total += c // mid
        if total >= N:
            break

    if total >= N:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
```

### 시도2

`ZeroDivisionError`가 발생해서 [yerimstar](https://velog.io/@yerimstar/%EB%B0%B1%EC%A4%80-1654%EB%B2%88-%EB%9E%9C%EC%84%A0-%EC%9E%90%EB%A5%B4%EA%B8%B0) 
님의 블로그를 참고하였다.

랜선들은 모두 자연수이기 때문에 `start`를 0으로 잡을 필요가 없었고, `start`을 1로 시작하니 문제 해결

```python
# https://www.acmicpc.net/problem/1654
# 랜선 자르기
import sys

input = sys.stdin.readline

K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]

start, end = 1, max(cables)
answer = -1
while start <= end:
    mid = (start + end) // 2
    total = 0

    for c in cables:
        total += c // mid
        if total >= N:
            break

    if total >= N:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
```
