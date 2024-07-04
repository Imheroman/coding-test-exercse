# n, m = map(int, input().split())
# test = [list(map(int, input().split())) for _ in range(n)]
n, m = 15, 14

graphs = [
    list(map(int, "00000111100000")),
    list(map(int, "11111101111110")),
    list(map(int, "11011101101110")),
    list(map(int, "11011101100000")),
    list(map(int, "11011111111111")),
    list(map(int, "11011111111100")),
    list(map(int, "11000000011111")),
    list(map(int, "01111111111111")),
    list(map(int, "00000000011111")),
    list(map(int, "01111111111000")),
    list(map(int, "00011111111000")),
    list(map(int, "00000001111000")),
    list(map(int, "11111111110011")),
    list(map(int, "11100011111111")),
    list(map(int, "11100011111111")),
]


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graphs[x][y] != 0:
        return False

    graphs[x][y] = 1
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print("result:", result)




