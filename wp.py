import pyautogui as gui
import time
message = input("Enter your message: ")
number = input("Enter your number: ")

time.sleep(2)
for i in range(int(number)):
    gui.typewrite(message)
    gui.press('Enter')
