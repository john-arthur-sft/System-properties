from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import os 


root = Tk()
root.title("System Properties")
root.geometry('502x505')
root.resizable(False,False)
root.iconbitmap("media/Logo.ico")

root.configure(background="black")

canvas1 = Canvas(root,bg="tan",width=491.5,height=100,
                 bd=2,relief = 'groove').place(x = 1,y = 2)

canvas2 = Canvas(root,bg="#CDAF95",width = 491.5,height = 300,
                 bd = 2,relief = 'groove').place(x = 1,y = 112)

canvas3 = Canvas(root,bg="#FFE4B5",width = 491.5,height = 70,
                 bd = 2,relief = 'groove').place(x = 1,y = 422)

header = Label(root,text="System properties",font=("Courier",25,"bold"),
               fg = "#33A1C9",bg='tan').pack(padx=80,pady=35)


#time = sd.askinteger("Time","Please enter the time in seconds for the action to be completed.")
# creating function
# function starts

def shutdown():
    time = sd.askinteger("Time","Please enter the time in seconds for the action to be completed.")
    os.system(f'shutdown /s /t {time}')
    exit()

def restart():
    time = sd.askinteger("Time","Please enter the time in seconds for the action to be completed.")
    os.system(f'shutdown /r /t {time}')
    exit()

def hibernate():
    os.system('shutdown /h')
    exit()

def abort():
    os.system('shutdown /a')
    exit()
    
def GUI():
    os.system('shutdown /i')
    exit()

def advance():
    os.system('shutdown /o /r')
    exit()

def logoff():
    time = sd.askinteger("Time","Please enter the time in seconds for the action to be completed.")
    os.system(f'shutdown /l /t {time}')
    exit()

def about():
    mb.showinfo("About","Programming Language : Python 3\nCreated by : John Arthur\nDate : 30/07/2021")

def help():
    mb.showinfo("Help","It is a simple GUI to perform some advance option \n\n\t 'Do no Play with this'")
    

shutdown = Button(canvas2,text="Shutdown",bd = 2,relief="raised",
                  font=("Arial",15,"bold"),bg="#C1CDCD",fg="#5E2612",width=10,
                  command=shutdown).place(x = 35,y = 125)

restart = Button(canvas2,text="Restart",bd = 2,relief="raised",
                  font=("Arial",15,"bold"),bg="#C1CDCD",fg="#5E2612",width=10,
                 command=restart).place(x = 175,y = 125)


LogOff = Button(canvas2,text="Log Off",bd = 2,relief="raised",
                  font=("Arial",15,"bold"),bg="#C1CDCD",fg="#5E2612",width=10,
                command=logoff).place(x = 315,y = 125)

hibernate = Button(canvas2,text="hibernate",bd = 2,relief="raised",
                  font=("Arial",15,"bold"),bg="#C1CDCD",fg="#5E2612",width=10,
                   command=hibernate).place(x = 35,y = 185)

GUI = Button(canvas2,text="GUI-control",bd = 2,relief="raised",
                  font=("Arial",15,"bold"),bg="#C1CDCD",fg="#5E2612",width=10,
             command=GUI).place(x = 175,y = 185)

abort = Button(canvas2,text="Abort",bd = 2,relief="raised",
                  font=("Arial",15,"bold"),bg="#C1CDCD",fg="#5E2612",width=10,
               command=abort).place(x = 315,y = 185)

advanced = Button(canvas2,text="advance-boot option",bd = 2,relief="raised",
                  font=("Arial",15,"bold"),bg="#C1CDCD",fg="#5E2612",width=20,
                  command=advance).place(x = 105,y = 275)

_help = Button(canvas2,text="Help",bd = 2,relief="raised",
                  font=("Arial",15,"bold"),bg="#C1CDCD",fg="#5E2612",width=10,
               command=help).place(x = 35,y = 365)

about = Button(canvas2,text="about",bd = 2,relief="raised",
                  font=("Arial",15,"bold"),bg="#C1CDCD",fg="#5E2612",width=10,
               command=about).place(x = 315,y = 365)

cancel = Button(canvas3,text="Exit",bd = 2,relief="ridge",
                  font=("Arial",15,"bold"),bg="#C1CDCD",fg="#5E2612",width=25,
                command=exit).place(x = 105,y = 435)

root.mainloop()
