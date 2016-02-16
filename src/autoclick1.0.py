#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyautogui, time, threading, sys
from tkinter import Tk, BOTH, LEFT, BOTTOM, RIGHT, TOP, Toplevel, BitmapImage, GROOVE, CENTER, Button, FLAT
from tkinter.ttk import Label, Style, Frame
import tkinter as tk

CLOSEBOX = """
#define close_width 10
#define close_height 10
static unsigned char close_bits[] = {
 0xFF, 0x03, 0x01, 0x02, 0x85, 0x02, 0x49, 0x02, 0x31, 0x02, 0x31, 0x02,
 0x49, 0x02, 0x85, 0x02, 0x01, 0x02, 0xFF, 0x03
};

"""

CLOSEHOVER = """
#define close_width 10
#define close_height 10
static unsigned char close_bits[] = {
  0xFF, 0x03, 0xFF, 0x03, 0x7B, 0x03, 0xB7, 0x03, 0xCF, 0x03, 0xCF, 0x03, 
  0xB7, 0x03, 0x7B, 0x03, 0xFF, 0x03, 0xFF, 0x03
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

class autoClicker(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        global running
        running = 0
                
        self.parent.overrideredirect(True)
        
        self.gripBar = BitmapImage(data=GRIPBAR)
        self.closeBox = BitmapImage(data=CLOSEBOX)
        self.closeHover = BitmapImage(data=CLOSEHOVER)
        
        self.barFrame = Frame(self)
        self.barFrame.pack(side=TOP, fill=BOTH, pady=(0,1))
        self.buttonFrame = Frame(self, relief=GROOVE)
        self.buttonFrame.pack(side=BOTTOM, fill=BOTH, padx=1, pady=(0,1))
        
        self.grip = Label(self.barFrame, image=self.gripBar)
        self.grip.image=self.gripBar
        self.grip.pack(side=LEFT, fill="x")
        self.grip.bind("<ButtonPress-1>", self.startMove)
        self.grip.bind("<ButtonRelease-1>", self.stopMove)
        self.grip.bind("<B1-Motion>", self.onMotion)
        
        self.closeButton = Label(self.barFrame, image=self.closeBox)
        self.closeButton.image=self.closeBox
        self.closeButton.pack(side=RIGHT, fill="none")
        self.closeButton.bind("<ButtonPress-1>", self.sysExit)
        self.closeButton.bind("<Enter>", self.onHover)
        self.closeButton.bind("<Leave>", self.onLeave)
        
        self.style = Style()
        self.style.theme_use("default")
        self.parent.wm_attributes("-topmost", 1)
        self.parent.resizable(0,0)

        self.startButton = Button(self.buttonFrame, text="Start", relief=FLAT, activebackground="lightgrey")
        self.startButton.pack(fill=BOTH, expand=1)
        self.startButton.bind("<Button-1>", self.startClick)
        self.startButton.bind("<space>", self.startClick)
                
        w = 116
        h = 40

        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.parent.config(bg="black")
        self.pack(fill="both", padx=1, pady=1)

    def onHover(self,event):
        event.widget.configure(image=self.closeHover)
    
    def onLeave(self,event):
        event.widget.configure(image=self.closeBox)

    def startMove(self,event):
        self.parent.x = event.x
        self.parent.y = event.y
        
    def onMotion(self, event):
        deltax = event.x - self.parent.x
        deltay = event.y - self.parent.y
        x = self.parent.winfo_x() + deltax
        y = self.parent.winfo_y() + deltay
        self.parent.geometry("+%s+%s" % (x, y))
        
    def stopMove(self, event):
        event.x = None
        event.y = None

    def sysExit(self, event):
        global running
        running = 0
        sys.exit()
            
    def startClick(self, event):
        global running
        if running == 0:
            running = 1
            event.widget.config(text="Stop")
            event.widget.flash()
            currentMouseX, currentMouseY = pyautogui.position()
            pyautogui.moveTo(currentMouseX, currentMouseY+50)
            threading.Thread(target=self.startLoop, args=()).start()
        else:
            running = 0
            event.widget.config(text="Start")
            event.widget.flash()
        time.sleep(0.2)
        return

    def startLoop(self):
        global running
        while running == 1:
           pyautogui.click()
           pyautogui.click(button="middle")
           time.sleep(0.0001)
        return
    
def main():
    root = Tk()
    app = autoClicker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
