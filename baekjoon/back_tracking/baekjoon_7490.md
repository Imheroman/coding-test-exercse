# [${number}번: title]()

1부터 N까지의 수를 오름차순으로 쓴 수열 1 2 3 ... N을 생각하자.

그리고 '+'나 '-', 또는 ' '(공백)을 숫자 사이에 삽입하자(+는 더하기, -는 빼기, 공백은 숫자를 이어 붙이는 것을 뜻한다). 이렇게 만든 수식의 값을 계산하고 그 결과가 0이 될 수 있는지를 살피자.

N이 주어졌을 때 수식의 결과가 0이 되는 모든 수식을 찾는 프로그램을 작성하라.

## 입출력

### 입력

첫 번째 줄에 테스트 케이스의 개수가 주어진다(<10).

각 테스트 케이스엔 자연수 N이 주어진다(3 <= N <= 9).

### 출력
각 테스트 케이스에 대해 ASCII 순서에 따라 결과가 0이 되는 모든 수식을 출력한다. 각 테스트 케이스의 결과는 한 줄을 띄워 구분한다.

## 예제

### 예제 입력 1

```text
2
3
7
```

### 예제 출력 1

```text
1+2-3

1+2-3+4-5-6+7
1+2-3-4+5+6-7
1-2 3+4+5+6+7
1-2 3-4 5+6 7
1-2+3+4-5+6-7
1-2-3-4-5+6+7
```

## 알고리즘 분류

- 구현
- 문자열
- 브루트포스 알고리즘
- 백트래킹

## 시도

### 시도1(32412kb, 144ms)

1 ~ N 까지 수에서 랜덤 연산자를 넣어 연산의 결과가 0인 식을 찾는 문제이다.

백트래킹을 이용하여 1부터 N까지 숫자를 증가시키면서 랜덤 연산자를 넣었고, 계속 값을 계산하면서 결과값을 파라미터로 넘겨주었다.

하지만, 왜인지 모르게도 띄어쓰기 연산에 대해 예제 출력과 일치하게 나오지 않았다.

30분 정도 고민하다가 그냥 다른 사람들의 코드를 찾아보았고, 다른 사람들은 `eval()` 함수를 이용하여 문자열을 그냥 바로 계산한 것을 보고 따라서 문제를 해결하였다.

```python
# https://www.acmicpc.net/problem/7490
# 0 만들기
import sys

input = sys.stdin.readline

OPERATORS = [" ", "+", "-"]


def back_tracking(current, size, repository=["1"]):
    if size + 1 == current:
        result = "".join(repository)
        ans = result.replace(' ', '')
        if eval(ans) == 0:
            print(result)
        return

    for operator in OPERATORS:
        repository.append(operator + str(current))
        back_tracking(current + 1, size, repository)
        repository.pop()


T = int(input())
for _ in range(T):
    N = int(input())
    back_tracking(2, N)
    print()
```

### 시도2

```python

```

### 시도3

```python

```

### 시도4

```python

```

## 정리

