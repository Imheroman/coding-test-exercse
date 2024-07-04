Y_DIC = {"L": -1, "R": 1}
X_DIC = {"U": -1, "D": 1}
POS_DIC = {"R": Y_DIC, "L": Y_DIC, "U": X_DIC, "D": X_DIC}

n = int(input())
plans = input().split()
x, y = 1, 1
# n = 5
# plans = "R R R U D D".split()

for plan in plans:
    print(x, y)
    pos = POS_DIC[plan]
    direction = pos[plan]

    if pos is X_DIC:
        if direction + x > 1:
            x += direction
    else:
        if direction + y > 1:
            y += direction

print(x, y)
