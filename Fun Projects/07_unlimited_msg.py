import pyautogui
import time
time.sleep(2)
count = 0
while count <= 100:
    pyautogui.typewrite("I Love you Jaan " + str(count))
    pyautogui.press("enter")
    count = count+1