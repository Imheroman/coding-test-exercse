# from sys import stdin

# ITERATORS = 2
# number_sum = [stdin.readline() for i in range(ITERATORS)]

# number = [int(digit) for digit in input()]
# students = [[*map(int, input().split())] for _ in range(N)]
# for student in students:
#     if student_clazz == student[clazz] and same_class_students[student_number] is not student:
#         same_class_students[student_number].add()

# for student in students[student_number]:
#     if student_clazz == student[clazz] and same_class_students[student_number] is not student:

# MAX_NUMBER = 1_000
# start, end = map(int, input().split())
# number_sequence = [number for number in range(1, end + 1) for _ in range(number)]
# print(sum(number_sequence[start-1:end]))

# print(str(123)[::-1])

# numbers = [[int(number) for number in input()] for _ in range(N)]

N, Q = map(int, input().split())
music = [int(input()) for _ in range(N)]

for _ in range(Q):
    question = int(input())
    answer = 1

    for index in range(1, N + 1):
        if sum(music[:index]) > question:
            break
        answer += 1

    print(answer)


# question = [int(input())for _ in range(Q)]
#
# for _ in range(N):


# numbers = list([*map(int, input().split())]for _ in range(N))
# numbers = []
#
# for i in range(N):
#     for number in input():
#         numbers.append(*map(int, number))
#
#     print(numbers)
