hours = int(input())
minutes = int(input())
minutes += 15

if minutes > 59:
    hours += 1
    minutes -= 60
# 23 : 50 + 0:15 = 24:05  = 0:05

if hours > 23:
    hours = 0

if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")
