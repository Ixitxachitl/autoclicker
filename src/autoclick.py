#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyautogui, time, threading
from tkinter import Tk, BOTH, RIGHT, LEFT
from tkinter.ttk import Frame, Button, Style
import tkinter as tk

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
    
    def initUI(self):
        global running
        running = 0
        self.parent.title("Auto-Clicker")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=True)
        self.parent.bind("<Escape>", self.bindExit)

        closeButton = Button(self, text="Close", command=self.sysExit)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        startButton = Button(self, text="Start", command=self.startClick)
        startButton.pack(side=LEFT, padx=5, pady=5)
        startButton.bind("<Button-1>", self.buttonText)

    def bindExit(self, e):
        self.sysExit()
        return
    
    def sysExit(self):
        global running
        running = 0
        self.quit()
        
    def buttonText(self, event):
        if event.widget["text"] == "Start":
            event.widget.config(text="Stop")
        else:
            event.widget.config(text="Start")
            
    def startClick(self):
        global running
        if running == 0:
            running = 1
            currentMouseX, currentMouseY = pyautogui.position()
            pyautogui.moveTo(currentMouseX+50, currentMouseY+50)
            threading.Thread(target=self.startLoop, args=()).start()
        else:
            running = 0
            time.sleep(0.5)

    def startLoop(self):
        global running
        while running == 1:
           pyautogui.click()
           pyautogui.click(button='middle')
           time.sleep(0.0001)

def main():
    root = Tk()
    root.wm_attributes("-topmost", 1)
    root.resizable(0,0)
    app = Example(root)
    w = 200 # width for the Tk root
    h = 30 # height for the Tk root

    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.mainloop()

if __name__ == '__main__':
    main()