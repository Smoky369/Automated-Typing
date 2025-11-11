
# Code by: Manish Pathak
# Instagram : manish_pathak369
import pyautogui
import time

time.sleep(5)  # Wait for 5 seconds before starting
for i in range(108):  # Loop to type 108 times
    pyautogui.typewrite("Hello World!")
    pyautogui.press("enter")