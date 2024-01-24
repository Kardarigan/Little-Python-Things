import datetime
from playsound import playsound

timeNow = datetime.datetime.now()

print(timeNow)
alarmHour = int(input("Enter The Hour: "))
alarmMinute = int(input("Enter The Minute: "))
alarmSecond = int(input("Enter The Second: "))
alarmMidday = input("Ante Meridies or Post Meridiem: ")

if alarmMidday == "pm":
    alarmHour += 12

while True:
    timeNow = datetime.datetime.now()
    if alarmHour == timeNow.hour and alarmMinute == timeNow.minute and alarmSecond == timeNow.second:
        print("Time is Up!")
        playsound("greedy.mp3")
        break