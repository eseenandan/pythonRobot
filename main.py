from testing import whatsApp
from chatGBT import chatGBT
import time
import pywhatkit
import pyautogui

pywhatkit.sendwhatmsg_instantly(phone_no="+15024963632", message="To stop the program, please enter 'stop program' to terminate the program. Until then, message whatever you want. This is an automated message. I am just a bot :)")
time.sleep(10)
count = 1
textMessaging = whatsApp(count)
while True: 
    textMessaging.getMessageAtStart()
    count = count + 1
    print(count)
    if textMessaging.stopProgram == True:
        pyautogui.typewrite("Program has been terminated. Thanks for using the program. Please message back to restablish connection.")
        pyautogui.hotkey('enter')
        break
    else:
        time.sleep(5)
        chat = chatGBT()
        chat.copyGBT()
        
        

# if the point at where the message recieved is white then copy the message 
# for multiple people we can do if the points at a position are blue then do a click then follow the order of operations 