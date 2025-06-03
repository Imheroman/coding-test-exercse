# [5671번: 호텔 방 번호](https://www.acmicpc.net/problem/5671)

선영이는 집 호수에 반복되는 숫자가 있는 경우에는 그 집에 사는 사람에게 불운이 찾아온다고 믿는다. 따라서, 선영이는 838호나 1004호와 같이 한 숫자가 두 번 이상 들어있는 집에는 절대 살지 않을 것이다.

2050년, 선영이는 한국에서 가장 돈이 많은 사람이 되었다. 그녀는 해변가에 새로운 호텔을 하나 지으려고 한다. 하지만, 투숙객에게 불운이 찾아오는 것을 피하기 위해서 반복되는 숫자가 없게 방 번호를 만들려고 한다.

정부는 선영이의 호텔 방 번호는 N보다 크거나 같고, M보다 작거나 같아야 한다는 조건을 걸고 신축 허가를 내주었다. 선영이의 새 호텔에는 방이 최대 몇 개 있을 수 있을까? (두 방이 같은 방 번호를 사용할 수 없다)

## 입출력

### 입력
입력은 여러 개의 테스트 케이스로 이루어져 있고, 한 줄이다. 각 줄에는 문제의 설명에 나와있는 N과 M이 주어진다. (1 ≤ N ≤ M ≤ 5000)

### 출력
각각의 테스트 케이스에 대해서 N보다 크거나 같고, M보다 작거나 같은 수 중에서 반복되는 숫자가 없는 것의 개수를 출력한다.

## 예제

### 예제 입력 1

```text
87 104
989 1022
22 25
1234 1234
```

### 예제 출력 1

```text
14
0
3
1
```

## 알고리즘 분류

- 수학
- 브루트포스 알고리즘

## 시도

### 시도1(34908kb, 1324ms)

입력된 `N ~ M` 범위의 숫자 중 각 자릿수를 보고 중복된 숫자가 있는지 확인하는 문제이다.

가장 쉽게 떠올릴 수 있는 `dictionary`를 이용해서 문제를 해결했다.

```python
import sys
import collections

input = sys.stdin.readline

while True:
    line = input().rstrip()

    if line == "":
        break

    N, M = map(int, line.split())
    answer = 0
    for current in range(N, M + 1):
        for value in collections.Counter(str(current)).values():
            if value > 1:
                break
        else:
            answer += 1

    print(answer)
```

### 시도2(34908kb, 632ms)

문제를 해결한 후 인터넷에서 다른 사람들의 코드를 구경해보니

[BackEnd Dev DreamTree It's](https://dreamtreeits.tistory.com/127)님의 블로그에서 `set()`을 이용해서
문제를 해결한 것을 보고 기가 막히다고 생각해서 작성해봤다.

```python
import sys

input = sys.stdin.readline

while True:
    line = input().rstrip()

    if line == "":
        break

    N, M = map(int, line.split())
    answer = 0
    for current in range(N, M + 1):
        if len(str(current)) == len(set(str(current))):
            answer += 1
    print(answer)
```

### 시도3

```python

```

### 시도4

```python

```

## 정리 및 소감
