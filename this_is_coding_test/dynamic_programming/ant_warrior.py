n = 4  # n = int(input())
storage = [1, 3, 1, 5]  # storage = list(map(int, input().split()))
memorization = [0] * (n + 1)

memorization[0] = storage[0]
# memorization[1] = max(storage[1], storage[0])
memorization[1] = storage[1]
for i in range(2, n):
    print(memorization)
    memorization[i] = max(memorization[i - 1], memorization[i - 2] + storage[i])

print(memorization[n - 1])




