import pyautogui
import time 
import pywhatkit
import win32api as fastMove
import win32con


pywhatkit.sendwhatmsg_instantly(phone_no="+15024963632", message="This is an automated message. You have 20 seconds to respond to use this feature.")
time.sleep(10)

# goes to the lowest position where the text is recieved then it goes to the bottom to grab text 
while True:
    position = pyautogui.position(1062,1708)
    px = pyautogui.pixel(position.x, position.y)
    top_y = position.y
    scrolledUp = False
    
    time.sleep(2)
    fastMove.SetCursorPos((position.x, position.y))
    position = pyautogui.position(position.x,position.y) # basically for getting the new position of cursor
    pyautogui.mouseDown(None,None,button='left')
    # if its not white it means user didnt respond 
    if px != (255,255,255):
        break
    
    
    # while the pixel is white on the bottom left of the message
    while px == (255,255,255):
        if position.y <= 373:
            position = pyautogui.position() # updates the coordinates that has the x and y 
            px = pyautogui.pixel(position.x , y) # updates the pixel checker to see if the pixels have changed
            top_y = position.y
            print(top_y)
            print(px)
            scrolledUp = True
        else:
            y = position.y - 20 # changes the y position up 20 pixels 
            fastMove.SetCursorPos((position.x, y))
            position = pyautogui.position() # updates the coordinates that has the x and y 
            px = pyautogui.pixel(position.x , y) # updates the pixel checker to see if the pixels have changed
            top_y = position.y
            print(position)
            
            
    
    # puts the cursor back into white area (47-63)
    # makes the left button stop highlighting 
    pyautogui.mouseUp()
    pyautogui.hotkey('ctrl', 'a')
    
    # apparently when you scroll up you need to increase the movement of the y position more 
    if scrolledUp == True:
        y = top_y + 80
    else:
        y = top_y + 20
        
    # changes the y position to be in the white area again
    fastMove.SetCursorPos((position.x, y))
    position = pyautogui.position()
    px = pyautogui.pixel(position.x, position.y)

    # holds the mouse left down so that it can copy the text 
    pyautogui.mouseDown(None,None,button="left")
    
    while px == (255,255,255):
        y = position.y + 20 # changes the y position down 20 pixels 
        fastMove.SetCursorPos((position.x, y))
        # pyautogui.moveTo(position.x, y) # updates the cursor 
        position = pyautogui.position(position.x, y) # updates the coordinates that has the x and y 
        px = pyautogui.pixel(position.x , y) # updates the pixel checker to see if the pixels have changed
        
    y = position.y + 80
    pyautogui.moveTo(position.x, y)  
    pyautogui.mouseUp()
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl','t')
    pyautogui.typewrite("https://chat.openai.com/chat")
    pyautogui.hotkey('enter')
    print("enter pressed")
    time.sleep(5)
    fastMove.SetCursorPos((1230,1769))
    fastMove.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    fastMove.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    pyautogui.hotkey('ctrl', 'v')
    print("paste pressed")
    break



