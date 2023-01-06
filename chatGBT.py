import pyautogui
import time
import win32api as fastMove
import win32con


class chatGBT:
    def __init__(self) -> None:
        pass

    def copyGBT(self):
        pyautogui.hotkey('enter')
        position = pyautogui.position()
        px = pyautogui.pixel(position.x, position.y)

        while True:
        # bot needs time to write out the stuff so if there isnt a reponse arrow dont do this code 
            if pyautogui.locateOnScreen('responseArrow.png', grayscale= False,confidence=0.90) != None:
                

                # while the pixel doesnt equal grey move the cursor up
                while px != (247, 247, 248):
                    print(px)
                    y = position.y - 80
                    fastMove.SetCursorPos((position.x, y))
                    position = pyautogui.position()
                    print(position)
                    px = pyautogui.pixel(position.x, position.y)

                # if the cursor is grey then scroll up unitl we do have our image
                while pyautogui.locateOnScreen('chatGBT.png', confidence=0.90) == None:
                        pyautogui.scroll(600)
                        position = pyautogui.position()
                        px = pyautogui.pixel(position.x, position.y)



            # Check if the cursor is still grey after breaking the loop
                if px == (247, 247, 248):
                    print("entered the if loop")
                    position = pyautogui.position()
                # supposed to scroll hold the mouse click down until it sees a mouseUp
                    pyautogui.mouseDown(position.x, position.y, button = "left")
                    time.sleep(0.25)
                    pyautogui.scroll(-50000)
                    time.sleep(0.25)
                    fastMove.SetCursorPos((position.x, position.y + 10000))
                    position = pyautogui.position()            

                    # while pixel is not white scroll down 
                    while px == (247,247,248):
                        print("entered the while loop")
                        fastMove.SetCursorPos((position.x,position.y + 30))
                        print(px)
                        px = pyautogui.pixel(position.x,position.y)
                        print(px)
                        position = pyautogui.position()
                
                    
                    pyautogui.mouseUp()
                    pyautogui.hotkey('ctrl', 'c')
                    print("copy text")
                    pyautogui.hotkey('ctrl', 'SHIFT', 'TAB')
                    pyautogui.hotkey('ctrl', 'v')
                    time.sleep(1)
                    pyautogui.hotkey('Enter')
                    
                    # exit out of the while loop
                    False
                    break
           
            #  if there is no regen button then we sleep 
            else:
                time.sleep(0.1)