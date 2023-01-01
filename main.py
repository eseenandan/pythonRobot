from testing import whatsApp
from chatGBT import chatGBT
import time
import pywhatkit
import win32api as fastMove
import win32con

# pywhatkit.sendwhatmsg_instantly(phone_no="+15024963632", message="This is an automated message")
# time.sleep(10)
# textMessaging = whatsApp()

# textMessaging.getMessageAtStart()
time.sleep(5)
fastMove.SetCursorPos((1062,1788))
chatGBT = chatGBT()
chatGBT.copyGBT()

# if the point at where the message recieved is white then copy the message 
# for multiple people we can do if the points at a position are blue then do a click then follow the order of operations 