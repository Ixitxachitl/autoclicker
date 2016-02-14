#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyautogui, time, threading, sys
from tkinter import Tk, BOTH, LEFT, BOTTOM, RIGHT, TOP, Toplevel, BitmapImage
from tkinter.ttk import Label, Button, Style, Frame
import tkinter as tk

CLOSEBOX = """
#define close_width 10
#define close_height 10
static unsigned char close_bits[] = {
 0xFF, 0x03, 0x01, 0x02, 0x85, 0x02, 0x49, 0x02, 0x31, 0x02, 0x31, 0x02,
 0x49, 0x02, 0x85, 0x02, 0x01, 0x02, 0xFF, 0x03
};

"""

GRIPBAR = """
#define grip_width 100
#define grip_height 10
static unsigned char grip_bits[] = {
0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
  0xFF,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x00,0xF8,0xFD,0x3F,0x27,0xFA,0x1C,0xE0,0x05,0x9F,0x17,0x7D,
  0xCF,0xFF,0xFB,0x01,0x80,0x28,0x22,0x22,0x10,0x04,0x44,0x90,
  0x04,0x11,0x00,0xF8,0xA9,0xAA,0x28,0x22,0x22,0x10,0x04,0x44,
  0x50,0x04,0x51,0x55,0xF9,0x55,0x95,0x2F,0x22,0xA2,0x17,0x04,
  0x44,0x70,0x1C,0x8F,0xAA,0xFA,0x01,0x80,0x28,0x22,0x22,0x10,
  0x04,0x44,0x90,0x04,0x11,0x00,0xF8,0xFD,0xBF,0xC8,0x21,0x1C,
  0xE0,0x7D,0x9F,0x17,0x7D,0xD1,0xFF,0xFB,0x01,0x00,0x00,0x00,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xF8,0xFF,0xFF,0xFF,
  0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF
};
"""

class autoClicker(Toplevel):
  
    def __init__(self, parent):
        Toplevel.__init__(self, parent)   
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        global running
        running = 0
                
        self.overrideredirect(True)
        
        gripBar = BitmapImage(data=GRIPBAR)
        closeBox = BitmapImage(data=CLOSEBOX)
        
        barFrame = Frame(self)
        barFrame.pack(side=TOP, fill="x", padx=1, pady=1)
        buttonFrame = Frame(self)
        buttonFrame.pack(side=BOTTOM, fill="x", padx=1, pady=(0,1))
        
        self.grip = Label(barFrame, image=gripBar)
        self.grip.image=gripBar
        self.grip.pack(side=LEFT, fill="x")
        self.grip.bind("<ButtonPress-1>", self.startMove)
        self.grip.bind("<ButtonRelease-1>", self.stopMove)
        self.grip.bind("<B1-Motion>", self.onMotion)
        
        self.closeButton = Label(barFrame, image=closeBox)
        self.closeButton.image=closeBox
        self.closeButton.pack(side=RIGHT, fill="none", padx=(0,1))
        self.closeButton.bind("<ButtonPress-1>", self.sysExit)
        
        self.style = Style()
        self.style.theme_use("default")
        self.wm_attributes("-topmost", 1)
        self.resizable(0,0)

        self.startButton = Button(buttonFrame, text="Start")
        self.startButton.pack(fill="both")
        self.startButton.bind("<Button-1>", self.startClick)
                
        w = 116
        h = 40

        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        
        self.protocol("WM_DELETE_WINDOW", self.sysExit)

        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.config(bg="black")

    def startMove(self,e):
        self.x = e.x
        self.y = e.y
        
    def onMotion(self, e):
        deltax = e.x - self.x
        deltay = e.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry("+%s+%s" % (x, y))
        
    def stopMove(self, e):
        e.x = None
        e.y = None

    def sysExit(self, e):
        global running
        running = 0
        sys.exit()
            
    def startClick(self, event):
        global running
        if running == 0:
            running = 1
            event.widget.config(text="Stop")
            currentMouseX, currentMouseY = pyautogui.position()
            pyautogui.moveTo(currentMouseX, currentMouseY+50)
            threading.Thread(target=self.startLoop, args=()).start()
        else:
            running = 0
            event.widget.config(text="Start")
            time.sleep(0.5)

    def startLoop(self):
        global running
        while running == 1:
           pyautogui.click()
           pyautogui.click(button="middle")
           time.sleep(0.0001)
        return

def main():
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", autoClicker.sysExit)   
    app = autoClicker(root)
    root.withdraw()    
    root.mainloop()

if __name__ == "__main__":
    main()
