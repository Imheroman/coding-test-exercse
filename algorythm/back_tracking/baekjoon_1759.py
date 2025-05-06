# https://www.acmicpc.net/problem/1759
# 암호 만들기
import sys
import itertools

input = sys.stdin.readline

L, C = map(int, input().split())
characters = sorted(list(input().rstrip().split()))

# 조합을 만들어서, 모음의 갯수(변수 만들어서 갯수 카운트), 자음의 갯수 파악해서 되는 것들만 count
# 되면 ?

VOWELS = ['a', 'e', 'i', 'o', 'u']
answer = []
for combination in sorted(itertools.combinations(characters, L)):
    print("combination:", combination)
    vowel = 0  # 모음
    consonant = 0  # 자음
    for character in combination:
        if character in VOWELS:
            vowel += 1
        else:
            consonant += 1

    if vowel >= 1 and consonant >= 2:
        answer.append(list(combination))

for ans in answer:
    print("".join(ans))