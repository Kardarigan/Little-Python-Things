import time

seconds = input("Enter time in Seconds: ")

while True:
    try:
        seconds = int(seconds)
        break
    except:
        seconds = input("Please enter a Number: ")

while seconds > 0:
    print(seconds)
    seconds -= 1
    time.sleep(1)

print("Time is Up!")