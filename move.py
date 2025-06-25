import pyautogui
import time

time.sleep(10)
pyautogui.click('New meeting button.png')

time.sleep(2)
pyautogui.click('start meeting button.png')

time.sleep(3)
try:
    pyautogui.click('mute.png')
except pyautogui.ImageNotFoundException:
    print("Not muted")

try:
    pyautogui.click('vid.png')
except pyautogui.ImageNotFoundException:
    print("Video is on")


time.sleep(10)
pyautogui.click('Add button.png')


