import pyautogui
import time

fail = False
incomingCall = False
end = False

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


time.sleep(180) # wait till call fail
try:
    pyautogui.locateOnScreen('Call_Failure.png', confidence=0.8)
    fail = True
    print("Call failed, waiting for call...")

    if fail:
        closeButton = pyautogui.locateCenterOnScreen('close.png', confidence=0.8) 
        pyautogui.click(closeButton)


except pyautogui.ImageNotFoundException:
    fail = False
    print("Call successful")
    
# Wait for incoming call if the call failed
if fail:
    try:
        pyautogui.locateOnScreen('Incoming_Call.png', confidence=0.8)
        incomingCall = True
    except pyautogui.ImageNotFoundException:
        incomingCall = False
    
    while incomingCall == False:
        time.sleep(10) # Wait for the next call 
        try:
            pyautogui.locateOnScreen('Incoming_Call.png', confidence=0.8)
            x, y = pyautogui.locateCenterOnScreen('Accept_Call.png', confidence=0.8)
            pyautogui.click(x, y) # Accept the call
            print("Incoming call accepted")
            incomingCall = True
            fail = False
        except pyautogui.ImageNotFoundException:
            incomingCall = False

# Check if Video and mic is on
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
time.sleep(15)
pyautogui.moveTo(height/2, width/2, duration=1)
pyautogui.click('Menu.png', duration=1)
time.sleep(1)
pyautogui.click('FullScreen.png', duration=1)


# Wait for the call to end
try:
    pyautogui.locateOnScreen('Call_Ended.png', confidence=0.8)
    print("Call ended")
    end = True
except pyautogui.ImageNotFoundException:
    end = False

while end == False:
    time.sleep(60) # Wait for the call to end
    try:
        pyautogui.locateOnScreen('Call_Ended.png', confidence=0.8)
        print("Call ended")
        end = True
    except pyautogui.ImageNotFoundException:
        end = False

# Leave the call
endCall = pyautogui.locateCenterOnScreen('End.png', confidence=0.8) 
pyautogui.click(endCall)

time.sleep(5) 
closeButton = pyautogui.locateCenterOnScreen('Close_button.png', confidence=0.8) 
pyautogui.click(closeButton)

