def is_right_step(stepp):
    return 1 <= stepp <= 8


STEPS = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

# pos = "a1"
pos = input()
col = ord(pos[0]) - ord("a") + 1
row = int(pos[1])

result = 0
for step in STEPS:
    row_step = row + step[0]
    col_step = col + step[1]

    if is_right_step(row_step) and is_right_step(col_step):
        result += 1

print(result)
