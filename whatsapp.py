import pywhatkit
import datetime
import pyautogui
import time

# cannot use the web driver because you need to sign in using phone to continue the program
# will have to use the pyautogui to simulate mouse clicks





# get the current time
pywhatkit.sendwhatmsg_instantly(phone_no="+15024963632", message="This is an automated message")

time.sleep(20)


# highlights the message 
pyautogui.leftClick(1097,1684)
pyautogui.leftClick(1097,1684)
pyautogui.leftClick(1097,1684)


# copies users message and pastes it into chatGBT
pyautogui.hotkey('ctrl','c')
pyautogui.hotkey('ctrl','t')
pyautogui.typewrite("https://chat.openai.com/chat")
time.sleep(5)
pyautogui.hotkey('enter')
pyautogui.leftClick(1230,1769)
pyautogui.hotkey('ctrl', 'v')
# waits for response in sec
time.sleep(30)



# copying message from chat gbt
# moves to first available position to copy messages
# pyautogui.leftClick(1085,382)
# pyautogui.leftClick(1097,1684)
# pyautogui.leftClick(1097,1684)



# while True:
#     position = pyautogui.position()
#     print(pyautogui.position())
#     print(pyautogui.position())