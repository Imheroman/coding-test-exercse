T = 10

for problem in range(1, T + 1):
    N = int(input())
    dumps = list(map(int, input().split()))

    for _ in range(N):
        low = dumps.index(min(dumps))
        high = dumps.index(max(dumps))

        dumps[low], dumps[high] = dumps[low] + 1, dumps[high] - 1

    print(f"#{problem} {max(dumps) - min(dumps)}")