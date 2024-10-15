# 정수 n을 %3 == 0, %2 == 0, else -1 을 이용하여 최단 으로 계산하는 방법

def solution(current_number, number_list):
    number_list[current_number] = number_list[current_number - 1] + 1  # 기존의 숫자에서 1을 뺌. 1 == 횟수 증가

    if current_number % 2 == 0:
        number_list[current_number] = min(number_list[current_number],
                                          number_list[current_number // 2] + 1)  # 1을 뺀 값과 2로 나누어지는 결과 중 더 작은 숫자를 선택

    if current_number % 3 == 0:
        number_list[current_number] = min(number_list[current_number],
                                          number_list[current_number // 3] + 1)  # 1을 뺀 값과 3으로 나누어진 결과 중 더 작은 숫자를 선택


number = int(input())

MIN_RANGE = 2
MAX_RANGE = number + 1

repository = [0] * MAX_RANGE

for current in range(MIN_RANGE, MAX_RANGE):
    solution(current, repository)

print(repository[number])

number = int(input())

MIN_RANGE = 2
MAX_RANGE = number + 1

repository = [0] * MAX_RANGE

for current in range(MIN_RANGE, MAX_RANGE):
    solution(current, repository)

print(repository[number])
