import pyautogui
import time

time.sleep(15) # Wait for the browser to load
# Select the group
try:
    pyautogui.click('Select_Chat.png')
except pyautogui.ImageNotFoundException:
    print("Chat is already selected")

# Get the call
time.sleep(5)
x, y = pyautogui.locateCenterOnScreen('Vid_Call.png',confidence=0.8)
pyautogui.click(x,y)

time.sleep(5)
x, y = pyautogui.locateCenterOnScreen('CallButton.png',confidence=0.8)
pyautogui.click(x,y)

# Check if Video and mic is on
time.sleep(60) # Wait till the call is connected
try:
    pyautogui.click('Mute.png')
    print("Unmuted successfully")
except pyautogui.ImageNotFoundException:
    print("Not muted")

try:
    pyautogui.click('Vid.png')
    print("Video is turned on")
except pyautogui.ImageNotFoundException:
    print("Video is on")

# Go to full screen mode
height, width = pyautogui.size() # Find the resolution of the screen
pyautogui.moveTo(height/2, width/2, duration=1)
pyautogui.click('Menu.png', duration=1)
time.sleep(1)
pyautogui.click('FullScreen.png', duration=1)



