import pyautogui
import time

time.sleep(5)
try:
    pyautogui.click('Select_Chat.png')
except pyautogui.ImageNotFoundException:
    print("Chat is already selected")

time.sleep(5)
x, y = pyautogui.locateCenterOnScreen('Vid_Call.png',confidence=0.8)
pyautogui.click(x,y)

time.sleep(3)
x, y = pyautogui.locateCenterOnScreen('CallButton.png',confidence=0.8)
pyautogui.click(x,y)

try:
    pyautogui.click('Mute.png')
except pyautogui.ImageNotFoundException:
    print("Not muted")

try:
    pyautogui.click('Vid.png')
except pyautogui.ImageNotFoundException:
    print("Video is on")



