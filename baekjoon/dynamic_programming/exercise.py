"""
어떤 수열의 연속 부분 수열에 같은 길이의 펄스 수열을 각 원소끼리 곱하여 연속 펄스 부분 수열을 만들려 합니다.
펄스 수열이란 [1, -1, 1, -1 …] 또는 [-1, 1, -1, 1 …] 과 같이 1 또는 -1로 시작하면서 1과 -1이 번갈아 나오는 수열입니다.
예를 들어 수열 [2, 3, -6, 1, 3, -1, 2, 4]의 연속 부분 수열 [3, -6, 1]에 펄스 수열 [1, -1, 1]을 곱하면
연속 펄스 부분수열은 [3, 6, 1]이 됩니다. 또 다른 예시로 연속 부분 수열 [3, -1, 2, 4]에 펄스 수열 [-1, 1, -1, 1]을 곱하면
연속 펄스 부분수열은 [-3, -1, -2, 4]이 됩니다.
정수 수열 sequence가 매개변수로 주어질 때, 연속 펄스 부분 수열의 합 중 가장 큰 것을 return 하도록 solution 함수를 완성해주세요.
"""


# https://howudong.tistory.com/210 보고 다시 풀어보기
# https://school.programmers.co.kr/learn/courses/30/lessons/161988


def solution(sequence):
    sequence_length = len(sequence)
    dp = [-999999999] * sequence_length
    positive_sequence = [0] * sequence_length
    negative_sequence = [0] * sequence_length

    for index, origin in enumerate(sequence):
        positive_turn = (-1) ** index
        negative_turn = positive_turn * - 1

        positive_sequence[index] = sequence[index] * positive_turn
        negative_sequence[index] = sequence[index] * negative_turn

    dp[0] = max(negative_sequence[0], positive_sequence[0])

    for index in range(1, sequence_length):
        dp[index - 1] = max(dp[index - 1] + positive_sequence[index],
                            positive_sequence[index])

    for index in range(1, sequence_length):
        negative_max = max(dp[index - 1] + negative_sequence[index],
                           negative_sequence[index])

        if dp[index] < negative_max:
            dp[index] = negative_max

    return max(dp)


SEQUENCE = [2, 3, -6, 1, 3, -1, 2, 4]
# SEQUENCE = [2]
print(solution(SEQUENCE))

# DP: [8, 10, 3, 9, 8, 5, 6, 4]



