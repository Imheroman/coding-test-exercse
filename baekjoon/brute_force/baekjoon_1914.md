# 1914번: 하노이탑

세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 각 원판은 반경이 큰 순서대로 쌓여있다. 이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.

아래 그림은 원판이 5개인 경우의 예시이다.

## 입출력

### 입력

첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 100)이 주어진다.

### 출력

첫째 줄에 옮긴 횟수 K를 출력한다.

N이 20 이하인 입력에 대해서는 두 번째 줄부터 수행 과정을 출력한다. 
두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데, 
이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다. 
N이 20보다 큰 경우에는 과정은 출력할 필요가 없다.

## 예제

### 예제 입력 1

```text
3
```

### 예제 출력 1

```text
7
1 3
1 2
3 2
1 3
2 1
2 3
1 3
```

## 시도

### 시도1

대학교 데이터구조 수업 시간에 다뤄본 적 있던 문제여서 재귀를 이용하여 푸는 문제라는 걸 알고 접근하였다.

하지만, 어떻게 해결했는지 기억이 안 나서 시간을 오래 쓰는 것 보다는 다른 사람들의 코드를 참고하기로 했다.

[studio.han](https://stdio-han.tistory.com/83)님의 블로그를 참고하여 풀었고, 
직접 손으로 재귀 코드를 실행해가며 확인하였는데, 머리가 좋은 편이 아니라서 그런지 아직 재귀의 재귀는 어려운 것 같다.  

```python
# https://www.acmicpc.net/problem/1914
# 하노이탑
import sys

input = sys.stdin.readline


def hanoi(n, one, two, three):
    if n == 1:
        print(one, three)
        return

    hanoi(n - 1, one, three, two)
    print(one, three)
    hanoi(n - 1, two, one, three)


def get_move_count(n):
    return 2 ** n - 1


N = int(input()) 
# N = 3
print(get_move_count(N))  # 모든 원판 이동 횟수는 N^2 - 1의 값이 나온다.

if N <= 20:
    hanoi(N, 1, 2, 3)
```

### 시도2

더 이해를 해보려고 봤으나, 이해가 안 돼서 추가로 다른 사람의 코드를 더 찾아보니,
[mingguriguri](https://velog.io/@miiingirok/백준-1914.-하노이탑-Python#내-코드-보완) 님의 블로그에서 
[밤샘공부](https://study-all-night.tistory.com/6) 님의 블로그를 참고하여 문제를 해결한 코드를 봤다.

**밤샘공부**님의 코드는 파라미터가 3개가 아닌 2개를 이용하여 문제를 해결하였고, 
나머지 타워의 위치를 알아내는 부분만 이해하면 문제를 해결하기가 더 수월했다. 

```python
# https://www.acmicpc.net/problem/1914
# 하노이탑
import sys

input = sys.stdin.readline
SUM_TOTAL_TOWER_HEIGHT = 6


def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return

    another_tower = SUM_TOTAL_TOWER_HEIGHT - start - end

    hanoi(n - 1, start, another_tower)
    print(start, end)
    hanoi(n - 1, another_tower, end)


def get_move_count(n):
    return 2 ** n - 1  # 모든 원판 이동 횟수는 N^2 - 1의 값이 나온다.


N = int(input())
# N = 3
print(get_move_count(N))

if N <= 20:
    hanoi(N, 1, 3)
```

## 정리

