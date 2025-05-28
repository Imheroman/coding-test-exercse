# [1213번: 팰린드롬 만들기](https://www.acmicpc.net/problem/1213)

문제
임한수와 임문빈은 서로 사랑하는 사이이다.

임한수는 세상에서 팰린드롬인 문자열을 너무 좋아하기 때문에, 둘의 백일을 기념해서 임문빈은 팰린드롬을 선물해주려고 한다.

임문빈은 임한수의 영어 이름으로 팰린드롬을 만들려고 하는데, 임한수의 영어 이름의 알파벳 순서를 적절히 바꿔서 팰린드롬을 만들려고 한다.

임문빈을 도와 임한수의 영어 이름을 팰린드롬으로 바꾸는 프로그램을 작성하시오.

## 입출력

### 입력

첫째 줄에 임한수의 영어 이름이 있다. 알파벳 대문자로만 된 최대 50글자이다.

### 출력

첫째 줄에 문제의 정답을 출력한다. 만약 불가능할 때는 "I'm Sorry Hansoo"를 출력한다. 정답이 여러 개일 경우에는 사전순으로 앞서는 것을 출력한다.

## 예제

### 예제 입력 1

```text
AABB
```

### 예제 출력 1

```text
ABBA
```

### 예제 입력 2

```text
AAABB
```

### 예제 출력 2

```text
ABABA
```

### 예제 입력 3

```text
ABACABA
```

### 예제 출력 3

```text
AABCBAA
```

### 예제 입력 3

```text
ABCD
```

### 예제 출력 3

```text
I'm Sorry Hansoo
```

## 알고리즘 분류

- 구현
- 그리디 알고리즘
- 문자열

## 시도

### 시도1(시간 초과, Python3, Pypy3)

한 개의 문자열을 이용하여, 여러 문자를 만드는 것을 보고 당연히 백트래킹을 이용해서
문자열 조합을 만들어내면 될 것이라고 생각했다.

문자열의 길이는 최대 `50`이고, 시간 제한은 1초이지만 가능할 것이라고 추측만 했다.

하지만, 시간 초과가 발생했고, itertools를 이용하여 순열을 만들어봐도 시간 초과가 발생했다.

왜 그런지 확인해보기 위해서 대충 약 30개 이상의 문자로 문자열을 만들어 입력해봤고, 몇 십초가 지나도 출력이 안 됐다.

내 `back_tracking()` 코드를 확인해봤을 때, 만약 문자열의 길이가 50이라면 ? ->
50 * 49 * 48 * 47 * ... * 1 만큼 확인해봐야 한다고 생각이 들었고, 이는 곧 50!의 값으로 `3.04140932017×10⁶⁴`의 값이었다.
(알고리즘 초보라 정확한 식은 아니지만, 아무튼 큰 값이 나오는 것으로 추정)

결국 일단 시간초과 ,,

```python
# https://www.acmicpc.net/problem/1213
# 팰린드롬 만들기
import itertools
import sys

input = sys.stdin.readline

letters = sorted(list(input().rstrip()))


def is_palindrome(arr):
    for i in range(len(arr) // 2):
        if arr[i] != arr[(len(arr) - 1) - i]:
            return False
    return True


def back_tracking(arr, visited, current, size, repository=set()):
    if size == 0:
        global answer
        # print(*current)
        result = "".join(current)
        print(repository, end=' -> ')
        print(result)
        if result not in repository and is_palindrome(current):
            print(result)
            repository.add(result)
            answer.append(result)
        return

    for index in range(len(arr)):
        if not visited[index]:
            visited[index] = True
            back_tracking(arr, visited, current + [arr[index]], size - 1)
            visited[index] = False

    return


answer = []
back_tracking(letters, [False] * len(letters), [], len(letters))
# for permutation in itertools.permutations(letters, len(letters)):
#     print(permutation)
#     if is_palindrome(permutation):
#         answer.append("".join(permutation))

if answer:
    print(sorted(answer)[0])
else:
    print("I'm Sorry Hansoo")
```

### 시도2(32412kb, 36ms, Python3)

어떻게 여러 문자열 리스트를 현재 코드에서 시간을 줄여 생성할 수 있는지 생각해봤지만, 당장 떠오르는 아이디어가 없었다.

또한, 지금의 지식과 실력으로는 새로운 문자열 리스트를 손쉽게 만들기는 어렵다고 생각해서 구글에 풀이를 검색해봤고,

[SJ H](https://thisismi.tistory.com/entry/%EB%B0%B1%EC%A4%80-1213%EB%B2%88-%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC-%EB%A7%8C%EB%93%A4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A0%95%EB%8B%B5-%EC%BD%94%EB%93%9C)
님의 블로그를 보게 되었다.

팰린드롬의 조건은 홀수인 문자의 수가 2개 미만이여야한다. (이건 이 문제를 풀며 생각한 문제이긴 했지만, 적용을 못 했음 == 실력 부족)

또한, 문제의 조건은 사전 순서의 첫 번째 팰린드롬 문자열만 원하고 있다.

따라서, 미리 정렬한 문자열에 팰린드롬인지 판별하고, 각자에 맞는 풀이를 해주면 된다.

1. 팰린드롬일 시 정렬된 문자열로(사전 순서이기 때문에) 문자열 크기의 반만 가지고 미리 문자열을 만든다.
  1. 홀수인 수가 있으면 홀수인 수를 추가
2. 나머지 문자열이 가진 수는 동일하기 때문에, 이미 만들어진 문자열을 뒤집는다.

를 이용하여 문제를 해결

```python
# https://www.acmicpc.net/problem/1213
# 팰린드롬 만들기
import sys

input = sys.stdin.readline

letters = sorted(list(input().rstrip()))
dictionary = {chr(ord('a') + i): 0 for i in range(26)}
key_list = sorted(list(set(letters)))

odd = []
for key in key_list:
    count = letters.count(key)
    dictionary[key] = count
    if count % 2 != 0:
        odd.append(key)

    if len(odd) >= 2:
        print("I'm Sorry Hansoo")
        exit()

answer = ""
for key in key_list:
    for j in range(dictionary[key] // 2):
        answer += key

if odd:
    print(answer + odd[0] + answer[::-1])
else:
    print(answer + answer[::-1])
```