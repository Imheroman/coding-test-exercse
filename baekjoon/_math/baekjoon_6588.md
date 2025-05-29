# [6588번: 골드바흐의 추측](https://www.acmicpc.net/problem/6588)

1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.

> 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.

예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다.
또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.

이 추측은 아직도 해결되지 않은 문제이다.

백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.

## 입출력

### 입력

입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다. 테스트 케이스의 개수는 100,000개를 넘지 않는다.

각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다. (6 ≤ n ≤ 1000000)

입력의 마지막 줄에는 0이 하나 주어진다.

### 출력

각 테스트 케이스에 대해서, n = a + b 형태로 출력한다.
이때, a와 b는 홀수 소수이다. 숫자와 연산자는 공백 하나로 구분되어져 있다.
만약, n을 만들 수 있는 방법이 여러 가지라면, b-a가 가장 큰 것을 출력한다.
또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는 "Goldbach's conjecture is wrong."을 출력한다.

## 예제

### 예제 입력 1

```text
8
20
42
0
```

### 예제 출력 1

```text
8 = 3 + 5
20 = 3 + 17
42 = 5 + 37
```

## 알고리즘 분류

- 수학
- 정수론
- 소수 판정
- 에라토스테네스의 체

## 시도

### 시도1(시간 초과 - Python3, Pypy3)

4 이상의 짝수를 두 소수의 합으로 나타낼 수 있는지 판별하는 문제이다.

1. 에라토스테네스의 체를 이용하여, 소수를 미리 구하고
2. 반복문 2개를 이용하여 처음부터 마지막을 순회하며 방문한다.(b-a가 가장 큰 것을 구하여야하기 때문에 처음과 마지막 부터 탐색)
3. `flag`를 이용하여 정답을 찾았는지 확인 후 찾았으면 다음 숫자 입력

하지만, 시간 초과 ,,,,,

```python
import sys
import math

input = sys.stdin.readline

MAX_NUMBER = 1_000_001

prime_numbers = [True] * MAX_NUMBER

for i in range(2, int(math.sqrt(MAX_NUMBER)) + 1):
    if prime_numbers[i]:
        for j in range(i * i, MAX_NUMBER, i):
            prime_numbers[j] = False

while True:
    number = int(input())

    if number == 0:
        break

    flag = False
    for i in range(2, number):
        if prime_numbers[i]:
            for j in range(number, 1, -1):
                if prime_numbers[j] and number == i + j:
                    print(f"{number} = {i} + {j}")
                    flag = True
                    break
        if flag:
            break
```

### 시도2(시간 초과 - Python3, 119252kb, 408ms - Pypy3)

[염지현](https://velog.io/@yeomja99/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-6588%EB%B2%88-%EA%B3%A8%EB%93%9C%EB%B0%94%ED%9D%90%EC%9D%98-%EC%B6%94%EC%B8%A1)
님의 블로그를 보고 작성한 코드이다.

기존 내가 작성했던 시도1 코드와 다른 점은 반복문을 1개만 돌고, 3부터 시작해서 2씩 증가한다는 점이다.(홀수만 반복 -> 짝수에 짝수를 빼면 2 이상의 짝수가 되기 떄문에 소수가 될 수 없다.)

반복문을 1개만 사용하는 이유는 전체 소수를 돌 수 있고, 나머지 수는 어차피 `원래의 수 - 특정 소수`로 결정되기 때문이다.

```python
import sys

input = sys.stdin.readline

MAX_NUMBER = 1_000_001

prime_numbers = [True] * MAX_NUMBER

for i in range(2, int(MAX_NUMBER ** 0.5) + 1):
    if prime_numbers[i]:
        for j in range(i * i, MAX_NUMBER, i):
            prime_numbers[j] = False

while True:
    number = int(input())

    if number == 0:
        break

    for i in range(3, number, 2):
        if prime_numbers[i] and prime_numbers[number - i]:
            print(f"{number} = {i} + {number - i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")
```