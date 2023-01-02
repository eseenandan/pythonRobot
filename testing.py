import pyautogui
import time 
import pywhatkit
import win32api as fastMove
import win32con
import pyperclip as pc
import re


class whatsApp:
    def __init__(self, count):
        self.stopProgram = False
        self.count = count
        
    def getMessageAtStart(self):        
        # goes to the lowest position where the text is recieved then it goes to the bottom to grab text 
        self.copyTexts()
        copiedMessage = pc.paste()
        
        if 'stop program' in copiedMessage.lower():
            self.stopProgram = True
            pass   
        elif self.count == 1:
            time.sleep(0.2)
            pyautogui.typewrite("https://chat.openai.com/chat")
            pyautogui.hotkey('enter')
            print("enter pressed")
            
            # need time to connect first time you enter website if you havent logged in prior
            while True:
                if pyautogui.locateOnScreen('responseArrow.png', grayscale= False,confidence=0.90) != None:
                    pyautogui.hotkey('ctrl', 'v')
                    print("paste pressed")
                    break
            # fastMove.SetCursorPos((1230,1769))
            # fastMove.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            # time.sleep(0.01)
            # fastMove.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            
            # need to fix it so that the ctrl v can be pasted in there then we done
        else:
            while True:
                if pyautogui.locateOnScreen('responseArrow.png', grayscale= False,confidence=0.90) != None:
                    position = pyautogui.position()
                    fastMove.SetCursorPos((position.x,position.y - 25))
                    pyautogui.leftClick()
                    pyautogui.hotkey('ctrl', 'v')
                    break
        
    def copyTexts(self):
         # goes to the lowest position where the text is recieved then it goes to the bottom to grab text 
        while True:
            position = pyautogui.position(1062,1708)
            px = pyautogui.pixel(position.x, position.y)
            top_y = position.y
            scrolledUp = False
            
            count = 5
            if px == (255,255,255):
                fastMove.SetCursorPos((position.x, position.y))
                position = pyautogui.position(position.x,position.y) # basically for getting the new position of cursor
                pyautogui.mouseDown(None,None,button='left')
                
                
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
                copiedMessage = pc.paste()
                
                if 'stop program' in copiedMessage.lower():
                    self.stopProgram = True
                    False 
                    break
                
                # if we are going the the program only the first time 
                elif self.count == 1:
                    pyautogui.hotkey('ctrl','t')
                    False
                    break
                
                # after the program is ran once then we just do ctrl tab
                else:
                    pyautogui.hotkey('ctrl', 'tab')
                    False
                    break
             
            # if the position at the pixel is white just sleep and have it re run the while loop  
            elif px != (255,255,255):
                time.sleep(5)
                count = count + 1
            # if the count is greater than 5 just assume the person wants to quit  
            elif count > 500:
                self.stopProgram = True
                break