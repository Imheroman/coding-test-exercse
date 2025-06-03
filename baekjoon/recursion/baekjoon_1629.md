# [1629번: 곱셈](https://www.acmicpc.net/problem/1629)

자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

## 입출력

### 입력

첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

### 출력

첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.

## 예제

### 예제 입력 1

```text
10 11 12
```

### 예제 출력 1

```text
4
```

## 알고리즘 분류

- 수학
- 분할 정복을 이용한 거듭제곱

## 시도

### 시도1(시간 초과 - Python3, PyPy3)

A를 B만큼 곱한 후 C로 나눈 나머지를 구하는 문제이다.

궁금해서 그냥 문제대로 바로 작성해봤는데, 당연히 시간 초과(입력 크기가 2,147,483,647 이하이니까)

```python
import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

print(A ** B % C)
```

### 시도2(32412kb, 32ms - Python3)

[Hyeoks](https://velog.io/@junttang/BOJ-1629-%EA%B3%B1%EC%85%88-%ED%95%B4%EA%B2%B0-%EC%A0%84%EB%9E%B5-C)님의 블로그를 보고 작성한
코드이다.

재귀를 이용해서 문제를 해결했다.

제곱은 곱셈의 횟수이므로
2<sup>11</sup> = 2<sup>(1)</sup> * 2<sup>5</sup> * 2<sup>5</sup> 이다.

따라서 위와 같이 작성해줄 수 있다.

이 문제를 해결하는 핵심은 연산의 횟수를 계속해서 절반으로 줄여나간다는 점이다.

1. B가 1이 될 때 까지 계속해서 B를 2로 나누며 탐색한다.
2. B가 1이 되는 순간, `a % c`를 return한다.(1번 곱셈을 시작한 것임)
3. 나온 결과를 가지고 제곱을 해준다.
4. 만약 B가 홀수였다면 `result * a & c`를 한 번 더 해준다.

를 가지고 코드를 작성했다.

```python
# https://www.acmicpc.net/problem/1629
# 곱셈
import sys

input = sys.stdin.readline


def recursion(a, b, c):
    if b == 1:
        return a % c
    elif b == 0:
        return 1

    result = recursion(a, b // 2, c) % c
    result = result ** 2 % c
    if b % 2 == 1:
        result = result * a % c

    return result


A, B, C = map(int, input().split())
# A, B, C = 10, 11, 12
print(recursion(A, B, C))
```
