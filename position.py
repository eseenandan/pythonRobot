import pyautogui
import time 

while True:
    position = pyautogui.position()
    px = pyautogui.pixel(position.x, position.y)
    time.sleep(2)
    # print(px)
    # if the cursor is grey then scroll up until white 
    if px == (247, 247, 248): 
        while px == (247, 247, 248):
            pyautogui.scroll(10)
            px = pyautogui.pixel(position.x, position.y)
    # Scroll down when white is hit
    if px == (255, 255, 255):
        pyautogui.scroll(-35)
        px = pyautogui.pixel(position.x,position.y)
        print("the px should be grey ", px)
        break       

print("hello there")
position = pyautogui.position()
px = pyautogui.pixel(position.x,position.y)
print(px)
pyautogui.scroll(-5)
px = pyautogui.pixel(position.x, position.y)
print(px)
# Check if the cursor is still grey after breaking the loop
if px == (247, 247, 248):
    print("entered the if loop")
    position = pyautogui.position()
    # supposed to scroll hold the mouse click down until it sees a mouseUp
    pyautogui.mouseDown(position.x, position.y, button = "left")
    pyautogui.scroll(-5000)
    # the initial position is used for checking the scroll has reached the bottom
    time.sleep(1)
    # while pixel is not white scroll down 
    while px == (247,247,248):
        print("entered the while loop")
        pyautogui.moveTo(position.x,position.y + 30.0)
        print(px)
        px = pyautogui.pixel(position.x,position.y)
        print(px)
        position = pyautogui.position()
        
    if px == (255, 255, 255): 
        print("Color is equal to white again")
        pyautogui.scroll(20)
        px = pyautogui.pixel(position.x, position.y)
        pyautogui.mouseUp()
        pyautogui.hotkey('ctrl', 'c')
    