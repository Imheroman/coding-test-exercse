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