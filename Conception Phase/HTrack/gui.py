from tkinter import *

'''
Main window
'''
main = Tk()
main.title("HTrack App")
main.geometry("1024x512")
main.resizable(0,0)

'''
Main window toolbar
'''
profileMenu = Menubutton(main, text = "Profile")
profileMenu.grid()
profileMenu.menu = Menu(profileMenu, tearoff = 0)
profileMenu["menu"] = profileMenu.menu
cVar = IntVar()
aVar = IntVar()
profileMenu.menu.add(label = "New profile", variable = cVar)
profileMenu.menu.add(label = "Load profile", variable = aVar)
profileMenu.pack()