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
def new_profile():
   print("New profile...")

def load_profile():
   print("Load profile...")

menu = Menu(main)
profileMenu = Menu(menu, tearoff = False)
profileMenu.add_command(label = "New profile", command = new_profile)
profileMenu.add_command(label = "Load profile", command = load_profile)
menu.add_cascade(label = "Profile", menu = profileMenu)