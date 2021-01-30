exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes

difference = arrival_time - exam_time
print(difference)


if difference > 0:
    print("Late")
elif -30 <= difference <= 0:
    print("On time")
elif difference < -30:
    print("Early")


if difference != 0:
    # •	"mm minutes before the start" за идване по-рано с по-малко от час
    if -60 < difference < 0:
        print(f"{abs(difference)} minutes before the start")
# •	"hh:mm hours before the start" за подраняване с 1 час или повече.
#  Минутите винаги печатайте с 2 цифри, например "1:05”
    elif difference <= -60:
        hours = 0
        hours = abs(difference) // 60
        minutes = abs(difference) % 60
        if minutes < 10:
            print(f"{hours}:0{minutes} hours before the start")
        else:
            print(f"{hours}:{minutes} hours before the start")
# "mm minutes after the start" за закъснение под час;
    if difference > 0:
        if difference < 60:
            print(f"{difference} minutes after the start")
        elif difference >= 60:
            hours = 0
            hours = difference // 60
            minutes = difference % 60
            if minutes < 10:
                print(f"{hours}:0{minutes} hours after the start")
            else:
                print(f"{hours}:{minutes} hours after the start")
