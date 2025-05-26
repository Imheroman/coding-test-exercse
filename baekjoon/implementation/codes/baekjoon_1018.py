# https://www.acmicpc.net/problem/1018
# 체스판 다시 칠하기
import sys

input = sys.stdin.readline
BOARD_SIZE = 8

DEFAULT_WHITE_BOARD = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]

N, M = map(int, input().split())
graphs = [list(input().rstrip()) for _ in range(N)]

answer = 32  # 변화시킬 수 있는 최대 횟수
for i in range(N - BOARD_SIZE + 1):  # 8개를 뺀 만큼 (보드 크기가 8임)
    for j in range(M - BOARD_SIZE + 1):  # 8개를 뺀 만큼 (보드 크기가 8임)
        result = 0
        for row in range(i, i + BOARD_SIZE):
            for col in range(j, j + BOARD_SIZE):
                if graphs[row][col] != DEFAULT_WHITE_BOARD[row - i][col - j]:
                    result += 1

        # 기존의 답, W가 첫 인덱스로 시작한 답, 64(8 * 8 == 체스 최대 말 수) 중 W가 첫 인덱스로 시작된 값을 뺀 결과 == 검정이 먼저 시작한 값
        answer = min(answer, result, 64 - result)

print(answer)
