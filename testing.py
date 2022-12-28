import pyautogui
import time 
import pywhatkit



pywhatkit.sendwhatmsg_instantly(phone_no="+15024963632", message="This is an automated message. You have 20 seconds to respond to use this feature.")
time.sleep(10)

# goes to the lowest position where the text is recieved then it goes to the bottom to grab text 
while True:
    position = pyautogui.position(1062,1708)
    px = pyautogui.pixel(position.x, position.y)
    top_y = position.y
    
    if px != (255,255,255):
        break
    
    time.sleep(2)
    pyautogui.moveTo(position.x, position.y)
    while px == (255,255,255):
        y = position.y - 20 # changes the y position
        pyautogui.moveTo(position.x, y) # updates the cursor 
        position = pyautogui.position(position.x, y) # updates the coordinates that has the x and y 
        px = pyautogui.pixel(position.x , y) # updates the pixel checker to see if the pixels have changed
        top_y = position.y
        print(position)
    
    y = top_y + 20
    pyautogui.moveTo(position.x, y)
    position = pyautogui.position(position.x, y)
    pyautogui.moveTo(position.x, y)
    px = pyautogui.pixel(position.x, y)
    pyautogui.mouseDown(None,None,button="left")
    
    while px == (255,255,255):
        y = position.y + 20 # changes the y position
        pyautogui.moveTo(position.x, y) # updates the cursor 
        position = pyautogui.position(position.x, y) # updates the coordinates that has the x and y 
        px = pyautogui.pixel(position.x , y) # updates the pixel checker to see if the pixels have changed
        
    y = position.y + 40
    pyautogui.moveTo(position.x, y + 40)    
    pyautogui.mouseUp()
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl','t')
    pyautogui.typewrite("https://chat.openai.com/chat")
    pyautogui.hotkey('enter')
    print("enter pressed")
    time.sleep(5)
    pyautogui.moveTo(1230,1769,0.5)
    pyautogui.leftClick(1230,1769)
    pyautogui.hotkey('ctrl', 'v')
    print("paste pressed")
    break



