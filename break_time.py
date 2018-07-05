import webbrowser as wb
import time

minutes = input("How long (in minutes) before you would like to take a break?")

#  delay program for a 10 seconds
while True:
    print("The timer has started")
    time.sleep(int(minutes)*60)
    print("Get to work!!!")
    wb.open("https://www.youtube.com/watch?v=gxaCaHNQCRI")
    minutes = input("How long would you like your break to be(in minutes): ")
    while not minutes.isnumeric():
        minutes = input("How long would you like your break to be(in minutes): ")
    time.sleep(int(minutes)*60)
    wb.open("https://www.youtube.com/watch?v=wnHW6o8WMas")
    print("Get to work!!!")