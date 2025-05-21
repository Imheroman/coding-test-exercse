# [2023번: 신기한 소수](https://www.acmicpc.net/problem/2023)

수빈이가 세상에서 가장 좋아하는 것은 소수이고, 취미는 소수를 가지고 노는 것이다. 요즘 수빈이가 가장 관심있어 하는 소수는 7331이다.

7331은 소수인데, 신기하게도 733도 소수이고, 73도 소수이고, 7도 소수이다. 즉, 왼쪽부터 1자리, 2자리, 3자리, 4자리 수 모두 소수이다! 수빈이는 이런 숫자를 신기한 소수라고 이름 붙였다.

수빈이는 N자리의 숫자 중에서 어떤 수들이 신기한 소수인지 궁금해졌다. N이 주어졌을 때, 수빈이를 위해 N자리 신기한 소수를 모두 찾아보자.

## 입출력

### 입력

첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다.

### 출력

N자리 수 중에서 신기한 소수를 오름차순으로 정렬해서 한 줄에 하나씩 출력한다.

## 예제

### 예제 입력 1

```text
4
```

### 예제 출력 1

```text
2333
2339
2393
2399
2939
3119
3137
3733
3739
3793
3797
5939
7193
7331
7333
7393
```

## 알고리즘 분류

- 수학
- 정수론
- 백트래킹
- 소수 판정

## 시도

### 시도1(메모리초과)

첫 번째 수부터 전체 수까지 가는 중 모든 수가 소수인 수를 구하는 문제이다.

소수라고 하자마자 '에라토스테네스의 체'가 떠올랐고 바로 적용해 봤으나,
n이 최대 8이라서 그런지, is_decimal 부분에서 메모리 초과가 발생했다.

```python
# https://www.acmicpc.net/problem/2023
# 신기한 소수
import math
import sys

input = sys.stdin.readline

n = int(input())
start = 1 * 10 ** (n - 1)
end = 1 * 10 ** n - 1

is_decimal = [True] * (end + 1)
is_decimal[0], is_decimal[1] = False, False
for i in range(2, int(math.sqrt(end)) + 1):
    if is_decimal[i]:
        for j in range(i + i, end + 1, i):
            is_decimal[j] = False

while start <= end:
    decimal = True
    for i in range(n):
        if not is_decimal[start // 10 ** i]:
            decimal = False
            break
    if decimal:
        print(start)

    start += 1
```

### 시도2(시간 초과)

블로그를 검색해보고, 최대한 내 코드를 살려서 문제를 해결해보고 싶어 소수 판별하는 부분만 수정해서 다시 제출해봤으나, 시간 초과

```python
# https://www.acmicpc.net/problem/2023
# 신기한 소수
import math
import sys

input = sys.stdin.readline

n = int(input())

start = 1 * 10 ** (n - 1)
end = 1 * 10 ** n - 1

_max = int(math.sqrt(end))
is_decimal = [True] * (_max + 1)
is_decimal[0], is_decimal[1] = False, False
for i in range(2, _max + 1):
    if is_decimal[i]:
        for j in range(i + i, _max + 1, i):
            is_decimal[j] = False

while start <= end:
    decimal = True
    for i in range(n):
        current = start // 10 ** i

        if current == 1:
            decimal = False
            continue

        for j in range(2, int(math.sqrt(current)) + 1):
            if current % j == 0:
                decimal = False
                break
        if not decimal:
            break
    if decimal:
        print(start)

    start += 1
```

### 시도3(34536kb, 40ms)

[감사쟁이](https://devjoy.tistory.com/245)님의 블로그를 보고 작성한 코드

1. `dfs`를 이용해서 소수를 계속해서 생성한다.
2. 작성한 수가 소수인지 판별하고
3. n에 맞는 길이라면, 답에 추가한다.

```python
# https://www.acmicpc.net/problem/2023
# 신기한 소수
import math
import sys

input = sys.stdin.readline

ODD_NUMBERS = ['1', '3', '5', '7', '9']
PRIME_NUMBER = ['2', '3', '5', '7']

n = int(input())
answer = []


def is_prime_number(current):
    if current <= 1:  # 1보다 작은 수는 소수가 아님
        return False

    for divisor in range(2, int(math.sqrt(current)) + 1):  # 제곱근까지 수를 구함
        if current % divisor == 0:  # 현재수가 제곱근까지 나누어지는 수가 있으면, 소수가 아님
            return False
    return True


def generate_prime_number(number, size, result):
    if not is_prime_number(int(number)):
        return  # 소수가 아니면 그냥 끝냄

    if size == len(number):
        result.append(number)
        return

    for odd_number in ODD_NUMBERS:  # 홀수를 계속해서 더한다.
        generate_prime_number(number + odd_number, size, result)


for prime_number in PRIME_NUMBER:
    generate_prime_number(prime_number, n, answer)

for ans in answer:
    print(ans)
```