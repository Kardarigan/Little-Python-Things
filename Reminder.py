import schedule
import time
import win10toast

message = input('Enter your message sire: ')
theTime = int(input('Minutes : '))
toaster = win10toast.ToastNotifier()

def send_notification():

    message = ''
    title = "A Message from Lord of Wallachia"    
    toaster.show_toast(title, message, duration=3)

schedule.every(theTime).minutes.do(send_notification) 

while True:
    schedule.run_pending()
    time.sleep(1)
