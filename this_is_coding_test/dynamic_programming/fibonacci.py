def recursive_fibonacci(n):  # 문제점 == 함수의 호출 값이 커질수록 중복 연산이 늘어난다. -> 30 정도를 넘기게 되면 연산의 횟수가 기하급수적으로 상승하기 시작함
    if n <= 2:
        return 1

    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def dynamic_fibonacci(n, memorization=[0]*300000):
    if n <= 2:
        return 1

    if memorization[n] == 0:
        memorization[n] = dynamic_fibonacci(n-1) + dynamic_fibonacci(n-2)

    return memorization[n]


def fibonacci(n, memorization=[0]*300000):
    memorization[2] = memorization[1] = 1

    for index in range(2, n + 1):
        memorization[index] = memorization[index - 1] + memorization[index - 2]

    return memorization[n]


print("recursive:", recursive_fibonacci(10))
print("dynamic:", dynamic_fibonacci(50))
print("iterate:", fibonacci(50))
