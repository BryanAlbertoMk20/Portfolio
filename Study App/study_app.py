from tkinter import *
from AppOpener import open, close
import os

root = Tk()
root.title("Study App")
root.geometry("450x350")
#Buttons for Studying with Pycharm

def open_study_apps_py():
    open("Google Chrome",output=False)
    open("Notepad++",output=False)
    open("PyCharm Community Edition",match_closest=True,output=False)

def close_study_apps_py():
    os.system("taskkill /im chrome.exe /f")
    close("Notepad++",output=False)
    os.system("taskkill /im pycharm64.exe /f")

open_study_apps_button = Button(root, text="Start studies with PyCharm", command=open_study_apps_py)
open_study_apps_button.place(x=25, y=100)


close_study_apps_button = Button(root, text="Time to stop study with Pycharm", command=close_study_apps_py)
close_study_apps_button.place(x=200, y=100)


#Buttons for Studying with VScode

def open_study_apps_vs():
    open("Google Chrome",output=False)
    open("Notepad++",output=False)
    os.startfile(r"C:\Users\bryan\AppData\Local\Programs\Microsoft VS Code\Code.exe")

def close_study_apps_vs():
    os.system("taskkill /im chrome.exe /f")
    close("Notepad++",output=False)
    os.system("taskkill /im Code.exe /f")

open_study_apps_button = Button(root, text="Start studies with VScode", command=open_study_apps_vs)
open_study_apps_button.place(x=25, y=200)


close_study_apps_button = Button(root, text="Time to stop study with VScode", command=close_study_apps_vs)
close_study_apps_button.place(x=200, y=200)

root.mainloop()