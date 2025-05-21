# [1342번: 행운의 문자열](https://www.acmicpc.net/problem/1342)

민식이와 준영이는 자기 방에서 문자열을 공부하고 있다. 민식이가 말하길 인접해 있는 모든 문자가 같지 않은 문자열을 행운의 문자열이라고 한다고 한다. 준영이는 문자열 S를 분석하기 시작했다. 준영이는 문자열 S에
나오는 문자를 재배치하면 서로 다른 행운의 문자열이 몇 개 나오는지 궁금해졌다. 만약 원래 문자열 S도 행운의 문자열이라면 그것도 개수에 포함한다.

## 입출력

### 입력

첫째 줄에 문자열 S가 주어진다. S의 길이는 최대 10이고, 알파벳 소문자로만 이루어져 있다.

### 출력

첫째 줄에 위치를 재배치해서 얻은 서로 다른 행운의 문자열의 개수를 출력한다.

## 예제

### 예제 입력 1

```text
aabbbaa
```

### 예제 출력 1

```text
1
```

### 예제 입력 2

```text
ab
```

### 예제 출력 2

```text
2
```

### 예제 입력 3

```text
aaab
```

### 예제 출력 3

```text
0
```

### 예제 입력 4

```text
abcdefghij
```

### 예제 출력 4

```text
3628800
```

## 알고리즘 분류

- 브루트포스 알고리즘
- 백트래킹

## 시도

### 시도1(메모리 초과)

주어진 문자열로 앞 뒤 문자가 중복되지 않게 만든 문자열의 수를 구하는 문제이다.

`itertools.permutations()`를 이용해서 수열을 만든 후
`set()`을 이용해서 중복되지 않은 답을 골라내려고 했으나, 메모리 초과가 발생했다.

`abcdefghij`의 입력에 대해 `3628800`의 결과를 보고, 어느 정도 예상을 했지만, 결과가 궁금해서 일단 작성해보았지만 실패

```python
import sys
import itertools

input = sys.stdin.readline

letters = list(input().rstrip())
size = len(letters)
answer = set()
for permutation in itertools.permutations(letters, size):
    for index in range(1, size):
        if permutation[index - 1] == permutation[index]:
            break
    else:
        answer.add(permutation)

print(len(answer))
```

### 시도2(오답)

답으로 제출하지는 않았지만, `aabbbaa`의 입력에 대해 정답인 `1`이 아니라 `144`의 결과가 나온다.

이론상으로는 가능할 것 같지만, 수많은 `abababa`가 나오기 때문에, 그걸 골라내지 못 하는 것 같다.

```python
# https://www.acmicpc.net/problem/18429
# 근손실
import sys

input = sys.stdin.readline

line = list("aabbbaa")


# line = list("ab")
# line = list("aaab")
# line = list("abcdefghij")


def dfs(letters, pre, visited, size=0):
    if size == len(letters):
        return 1

    answer = 0
    for index in range(len(letters)):
        if letters[index] != pre and not visited[index]:
            visited[index] = True
            answer += dfs(letters, letters[index], visited, size + 1)
            visited[index] = False

    return answer


print(dfs(line, '', [False] * len(line)))
```

### 시도3(114072kb, 2332ms)

[Doyeon Kim](https://velog.io/@yammayamm/%EB%B0%B1%EC%A4%80-1342%EB%B2%88-%ED%96%89%EC%9A%B4%EC%9D%98-%EB%AC%B8%EC%9E%90%EC%97%B4-Silver-1-Python)
님의 블로그를 보고 작성한 코드이다.

다른 많은 사람들도 Dictionary를 이용해서 문제를 해결했다.

```python
# https://www.acmicpc.net/problem/18429
# 근손실
import sys
from collections import Counter

input = sys.stdin.readline

line = list(input().rstrip())
dictionary = Counter(line)


def dfs(letters, pre, size=0):
    global answer

    if size == len(letters):
        answer += 1
        return

    for key in dictionary.keys():
        if key == pre or dictionary[key] <= 0:
            continue
        # if key != pre and dictionary[key] > 0:
        dictionary[key] -= 1
        dfs(letters, key, size + 1)
        dictionary[key] += 1

    return


answer = 0
dfs(line, '')
print(answer)
```