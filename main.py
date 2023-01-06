from testing import whatsApp
from chatGBT import chatGBT
import time
import pywhatkit
import pyautogui
from tkinter import *



def submit():
    phoneNumber = entry.get()
    pywhatkit.sendwhatmsg_instantly(phone_no= phoneNumber, message="To stop the program, please enter 'stop program' to terminate the program. Until then, message whatever you want. This is an automated message. I am just a bot :)")
    time.sleep(10)
    count = 1
    textMessaging = whatsApp(count)
    chat = chatGBT()
    while True: 
        textMessaging.getMessageAtStart()
        count = count + 1
        print(count)
        if textMessaging.stopProgram == True:
            pyautogui.typewrite("Program has been terminated. Thanks for using the program. Please message back to restablish connection.")
            pyautogui.hotkey('enter')
            window.destroy()
            break
        else:
            time.sleep(2)
            chat.copyGBT()
            

def delete():
    entry.delete(0,END) #deletes the line of text

def backspace():
    entry.delete(len(entry.get())-1,END) #delete last character        

window = Tk()
window.title("Chat Bot Program")
label = Label(window,text="Phone Number: ")
label.config(font=("Times New Roman",30))
label.pack(side=LEFT)

submit = Button(window,text="submit",command=submit)
submit.pack(side = RIGHT)

delete = Button(window,text="delete",command=delete)
delete.pack(side = RIGHT)

backspace = Button(window,text="backspace",command=backspace)
backspace.pack(side = RIGHT)

entry = Entry()
entry.config(font=('Times New Roman',35)) #change font
entry.config(bg='#111111') #background
entry.config(fg='White') #foreground
entry.config(width=25) #width displayed in characters
entry.pack()
window.mainloop()




# # if the point at where the message recieved is white then copy the message 
# # for multiple people we can do if the points at a position are blue then do a click then follow the order of operations 