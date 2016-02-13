#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyautogui, time, threading, sys
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
        startButton = Button(self, text="Start")
        startButton.pack(side=LEFT, padx=5, pady=5)
        startButton.bind("<Button-1>", self.startClick)

    def bindExit(self, e):
        self.sysExit()
        return
    
    def sysExit(self):
        global running
        running = 0
        sys.exit()
            
    def startClick(self, event):
        global running
        if running == 0:
            running = 1
            event.widget.config(text="Stop")
            currentMouseX, currentMouseY = pyautogui.position()
            pyautogui.moveTo(currentMouseX+50, currentMouseY+50)
            threading.Thread(target=self.startLoop, args=()).start()
        else:
            running = 0
            event.widget.config(text="Start")
            time.sleep(0.5)

    def startLoop(self):
        global running
        while running == 1:
           pyautogui.click()
           pyautogui.click(button='middle')
           time.sleep(0.0001)
        return

def main():
    root = Tk()
    def on_closing():
        global running
        running = 0
        sys.exit()
    root.protocol("WM_DELETE_WINDOW",on_closing)    
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