# [11723번: 집합](https://www.acmicpc.net/problem/11723)

비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

- add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
- remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
- check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
- toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
- all: S를 {1, 2, ..., 20} 으로 바꾼다.
- empty: S를 공집합으로 바꾼다.

## 입출력

### 입력

첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.

둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

### 출력

check 연산이 주어질때마다, 결과를 출력한다.

## 예제

### 예제 입력 1

```text
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1
```

### 예제 출력 1

```text
1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0
```

## 알고리즘 분류

- 구현
- 비트마스킹

## 시도

### 시도1(32412kb, 4396ms)

여러 명령어들을 통해 한 개의 저장소를 관리하는 문제이다.

입력되는 숫자인 `X`의 범위가 `1~20`으로 지정되어있기 때문에 그냥 dict로 간단하게 해결했다.

`add` 명령어 입력 시 숫자를 1씩 저장했고, `remove` 시 0으로 변경하여 문제를 해결했다.

```python
# https://www.acmicpc.net/problem/11723
# 집합
import sys

input = sys.stdin.readline

M = int(input())
repository = {num: 0 for num in range(1, 21)}

for _ in range(M):
    line = input().split()
    operator = line[0]
    op = 0

    if len(line) == 2:
        op = int(line[1])

    if operator == "add":
        repository[op] = 1
    elif operator == "check":
        if repository[op] != 0:
            print(1)
        else:
            print(0)
    elif operator == "remove":
        repository[op] = 0
    elif operator == "toggle":
        if repository[op]:
            repository[op] = 0
        else:
            repository[op] = 1
    elif operator == "all":
        repository = {num: 1 for num in range(1, 21)}
    else:
        repository = {num: 0 for num in range(1, 21)}
```

### 시도2(32412kb, 3932ms)

[dragonh](https://dragon-h.tistory.com/28)님의 블로그 아이디어를 참고해서 작성한 코드이다.

`boolean`으로 관리해서 문제를 해결했다고 하셔서 가능해보여 바로 코드로 옮겼다.

```python
# https://www.acmicpc.net/problem/11723
# 집합
import sys

input = sys.stdin.readline

MAX_SIZE = 21

M = int(input())
repository = [False] * MAX_SIZE

for _ in range(M):
    line = input().split()
    operator = line[0]
    op = 0

    if len(line) == 2:
        op = int(line[1])

    if operator == "add":
        repository[op] = True
    elif operator == "check":
        print(int(repository[op]))
    elif operator == "remove":
        repository[op] = False
    elif operator == "toggle":
        repository[op] = not repository[op]
    elif operator == "all":
        repository = [True] * MAX_SIZE
    else:
        repository = [False] * MAX_SIZE
```

## 정리

[미니의 하루](https://coarmok.tistory.com/entry/파이썬python-백준-11723번-비트마스킹)님의 블로그에 비트마스크로 문제를 해결한 코드가 아래와 같이 있다.

```python

for _ in range(m):
    order = input().strip()
    try:
        com, num = order.split()
        num = int(num)
        if com == 'add':
            s = s | (0b1 << num)
        elif com == 'remove':
            s = s & ~(0b1 << num)
        elif com == 'check':
            if s & (0b1 << num):
                print(1)
            else:
                print(0)
        elif com == 'toggle':
            s = s ^ (0b1 << num)
    except:
        if order == 'all':
            s = 0b111111111111111111111  # 1부터 20까지 켜짐
        elif order == 'empty':
            s = 0b0
```

add, remove 등은 이해가 되는데, 아직 나머지 부분을 깊게 이해하지 못 했다.

이해하려 노력하면 어렵지 않게 이해할 수 있을 것 같지만, 피곤해서 그런지 자주 쓰일 일이 없을 것 같아서 귀찮다는 생각이 들어 깊이 이해하고 싶지 않아졌다,,

나중에 다시 공부해보도록 하자 !