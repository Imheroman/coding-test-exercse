# n, m = map(int, input().split())
# rice_cakes = list(map(int, input().split()))
n, m = [4, 6]
rice_cakes = [19, 15, 10, 17]

answer = 0
h = 0

while m != answer:
    h += 1
    answer = 0

    for rice_cake in rice_cakes:
        result = rice_cake - h
        if result > 0:
            answer += result

print(h)
