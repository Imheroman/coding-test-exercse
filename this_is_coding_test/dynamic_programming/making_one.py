# n = int(input())
n = 26

d = [0] * (n + 1)
divide_numbers = [2, 3, 5]

for index in range(2, n + 1):
    d[index] = d[index - 1] + 1

    for divide in divide_numbers:
        if d[index] % divide == 0:
            d[index] = min(d[index], d[index // divide] + 1)
print(d[n])
