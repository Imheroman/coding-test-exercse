# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AWT-lPB6dHUDFAVT&categoryId=AWT-lPB6dHUDFAVT&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1
# 햄버거 다이어트
# https://velog.io/@seungjae/SWEA-5215-%ED%96%84%EB%B2%84%EA%B1%B0-%EB%8B%A4%EC%9D%B4%EC%96%B4%ED%8A%B8-Python-DFS


def back_tracking(arr, scores, calories, size, current=0):
    global answer

    if calories > L:
        return

    answer = max(answer, scores)

    if size == 0:
        return

    score, calorie = arr[current]

    back_tracking(arr, scores + score, calories + calorie, size-1, current+1)
    back_tracking(arr, scores, calories, size-1, current+1)


T = int(input())
for problem in range(1, T + 1):
    N, L = map(int, input().split())
    answer = 0
    data = [list(map(int, input().split())) for _ in range(N)]
    # back_tracking(data, 0, N, 0, [False] * N)
    back_tracking(data, 0, 0, N)
    print(f"#{problem} {answer}")

"""
1
5 1000
100 200
300 500
250 300
500 1000
400 400

0, 2, 4
"""

# 내 코드
# import itertools
#
# T = int(input())
# for problem in range(1, T + 1):
#     N, L = map(int, input().split())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     answer = 0
#
#     for size in range(1, N + 1):
#         for combination in itertools.combinations(range(N), size):
#             total_score = 0
#             total_calorie = 0
#
#             for index in combination:
#                 score, calorie = data[index]
#                 total_calorie += calorie
#                 total_score += score
#
#                 if total_calorie > L:
#                     break
#
#                 answer = max(total_score, answer)
#
#     print(f"#{problem} {answer}")