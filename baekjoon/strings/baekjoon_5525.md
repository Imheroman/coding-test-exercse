# [${number}번: title]()

N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.

- P<sub>1</sub> IOI
- P<sub>2</sub> IOIOI
- P<sub>3</sub> IOIOIOI
- P<sub>N</sub> IOIOI...OI (O가 N개)

I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.

## 입출력

### 입력

첫째 줄에 N이 주어진다. 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다.

### 출력

S에 PN이 몇 군데 포함되어 있는지 출력한다.

## 제한

- 1 ≤ N ≤ 1,000,000
- 2N+1 ≤ M ≤ 1,000,000
- S는 I와 O로만 이루어져 있다.

## 서브테스크

| 번호 | 배점 | 제한                  |
|----|----|---------------------|
| 1  | 50 | N ≤ 100, M ≤ 10 000 |
| 2  | 50 | 추가적인 제약 조건이 없다.     |

## 예제

### 예제 입력 1

```text
1
13
OOIOIOIOIIOII
```

### 예제 출력 1

```text
4
```

![스크린샷 2025-05-30 오전 2.03.59.png](..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fj4%2Flffybpwx1j7f046vfs9dpx9r0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_MatZrV%2F%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202025-05-30%20%EC%98%A4%EC%A0%84%202.03.59.png)

### 예제 입력 2

```text
2
13
OOIOIOIOIIOII
```

### 예제 출력 2

```text
2
```

![스크린샷 2025-05-30 오전 2.04.15.png](..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fj4%2Flffybpwx1j7f046vfs9dpx9r0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_UCTH1E%2F%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202025-05-30%20%EC%98%A4%EC%A0%84%202.04.15.png)

## 알고리즘 분류

- 문자열

## 시도

### 시도1(50점 - Python3, PyPy3)

- `IOI` == 1(N)  
- `IOIOI` == 2(N)

와 같이 `I`로 시작하고 `OI`가 N회 반복되는 패턴의 횟수를 찾아서 출력하는 문제이다.

따라서

1. 현재 위치의 문자가 I이면
2. `I` + `OI`가 `N`회만큼 반복됐을 때
3. 현재 위치에서 N 까지 길이의 문자열과 동일하면
4. 1회 카운트한다.

로 문제를 해결했으나, 문제를 맞추긴 했지만, 시간 초과의 서브태스크에 걸려서 50점을 맞았다.

```python
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = list(input())

answer = 0
current = -1
while current < M:
    current += 1

    if S[current] != "I":
        continue

    if ''.join(S[current:current + 2 * N + 1]) == "I" + "OI" * N:
        current += 1
        answer += 1

print(answer)
```

### 시도2(33388kb, 332ms - Python3 / 112428kb, 116ms - PyPy3)

[Overthinking](https://aia1235.tistory.com/30)님의 블로그를 보고 작성한 코드이다.

반복문을 빨리 탈출하기 위해 여러 조건들을 걸어줬으나, 시간 초과를 벗어날 순 없었다.

다른 블로그를 참고해보니 보통 

1. `IOI`만 가지고 나온 횟수를 카운트하고,
2. `N`과 카운트 횟수가 동일해지면(== `I` + `OI` * `N`의 횟수가 되면) 
3. 정답의 크기를 1 늘리고, 1칸 추가로 이동(총 2칸을 이동하는 것임 -> 이미 `IOI`를 확인했으니까 다시 I로 이동)
4. 다음에 추가로 이어지는 문자열이 있는지 확인하기 위해 카운트를 1 감소
5. 만약 현재 값이 `O`면 카운트를 0으로 다시 초기화

으로 문제를 해결했다.

```python
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

current = answer = count = 0
while current < M:
    if S[current: current + 3] == "IOI":
        count += 1
        current += 1
    else:
        count = 0

    if count == N:
        answer += 1
        count -= 1

    current += 1

print(answer)
```

### 시도3

```python

```

### 시도4

```python

```

## 정리 및 소감
