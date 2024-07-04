MINUTES = 60
SECONDS = 60
GUESS_NUMBER = "3"

n = int(input())
count = 0

for hour in range(n+1):
    hour = str(hour)
    for minute in range(MINUTES):
        minute = str(minute)
        for second in range(SECONDS):
            second = str(second)
            if GUESS_NUMBER in hour + minute + second:
                count += 1

print(count)
