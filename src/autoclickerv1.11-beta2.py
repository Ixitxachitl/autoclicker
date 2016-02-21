#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyautogui, time, threading, sys
from tkinter import *
from tkinter.ttk import Label, Style, Frame
from system_hotkey import SystemHotkey
import tkinter as tk

LEFTCLICK = """
#define leftclick_width 30
#define leftclick_height 20
static const unsigned char leftclick_bits[] = {
  0x00,0xf8,0xff,0x3f,0x00,0xfe,0xff,0x3f,0x80,0x07,0x00,0x20,0xc0,0x01,0x00,
  0x20,0x60,0x00,0x00,0x20,0x30,0x00,0x00,0x20,0x18,0x00,0x00,0x20,0x0c,0x00,
  0x00,0x20,0x0c,0x00,0x00,0x20,0x06,0x00,0x00,0x20,0x06,0x00,0x00,0x20,0x03,
  0x00,0x00,0x20,0x03,0x00,0x00,0x20,0x03,0x00,0x00,0x20,0x03,0x00,0x00,0x20,
  0x03,0x00,0x00,0x20,0x03,0x00,0x00,0x20,0x03,0x00,0x00,0x20,0xff,0xff,0xff,
  0x3f,0xff,0xff,0xff,0x3f
};
"""

LEFTCLICKDOWN = """
#define leftclickdown_width 30
#define leftclickdown_height 20
static const unsigned char leftclickdown_bits[] = {
 0x00,0xf0,0xff,0x3f,0x00,0xfe,0xff,0x3f,0x80,0xff,0xff,0x3f,0xc0,0xff,0xff,
 0x3f,0xe0,0xff,0xff,0x3f,0xf0,0xff,0xff,0x3f,0xf8,0xff,0xff,0x3f,0xfc,0xff,
 0xff,0x3f,0xfc,0xff,0xff,0x3f,0xfe,0xff,0xff,0x3f,0xfe,0xff,0xff,0x3f,0xff,
 0xff,0xff,0x3f,0xff,0xff,0xff,0x3f,0xff,0xff,0xff,0x3f,0xff,0xff,0xff,0x3f,
 0xff,0xff,0xff,0x3f,0xff,0xff,0xff,0x3f,0xff,0xff,0xff,0x3f,0xff,0xff,0xff,
 0x3f,0xff,0xff,0xff,0x3f
};
"""

MIDDLECLICK = """
#define middleclick_width 30
#define middleclick_height 20
static const unsigned char middleclick_bits[] = {
  0xff,0xff,0xff,0x3f,0xff,0xff,0xff,0x3f,0x01,0x00,0x00,0x20,0x01,0x00,0x00,
  0x20,0x01,0x00,0x00,0x20,0x01,0x00,0x00,0x20,0x01,0x00,0x00,0x20,0x01,0x00,
  0x00,0x20,0x01,0x00,0x00,0x20,0x01,0x00,0x00,0x20,0x01,0x00,0x00,0x20,0x01,
  0x00,0x00,0x20,0x01,0x00,0x00,0x20,0x01,0x00,0x00,0x20,0x01,0x00,0x00,0x20,
  0x01,0x00,0x00,0x20,0x01,0x00,0x00,0x20,0x01,0x00,0x00,0x20,0xff,0xff,0xff,
  0x3f,0xff,0xff,0xff,0x3f
};
"""

MIDDLECLICKDOWN = """
#define middleclickdown_width 30
#define middleclickdown_height 20
static const unsigned char middleclickdown_bits[] = {
 0xff,0xff,0xff,0x3f,0xff,0xff,0xff,0x3f,0xff,0xff,0xff,0x3f,0xff,0xff,0xff,
 0x3f,0xff,0xff,0xff,0x3f,0xff,0xff,0xff,0x3f,0xff,0xff,0xff,0x3f,0xff,0xff,
 0xff,0x3f,0xff,0xff,0xff,0x3f,0xff,0xff,0xff,0x3f,0xff,0xff,0xff,0x3f,0xff,
 0xff,0xff,0x3f,0xff,0xff,0xff,0x3f,0xff,0xff,0xff,0x3f,0xff,0xff,0xff,0x3f,
 0xff,0xff,0xff,0x3f,0xff,0xff,0xff,0x3f,0xff,0xff,0xff,0x3f,0xff,0xff,0xff,
 0x3f,0xff,0xff,0xff,0x3f
};
"""

RIGHTCLICK = """
#define rightclick_width 30
#define rightclick_height 20
static const unsigned char rightclick_bits[] = {
  0xFF, 0xFF, 0x07, 0x00, 0xFF, 0xFF, 0x1F, 0x00, 0x01, 0x00, 0x78, 0x00, 
  0x01, 0x00, 0xE0, 0x00, 0x01, 0x00, 0x80, 0x01, 0x01, 0x00, 0x00, 0x03, 
  0x01, 0x00, 0x00, 0x06, 0x01, 0x00, 0x00, 0x0C, 0x01, 0x00, 0x00, 0x0C, 
  0x01, 0x00, 0x00, 0x18, 0x01, 0x00, 0x00, 0x18, 0x01, 0x00, 0x00, 0x30, 
  0x01, 0x00, 0x00, 0x30, 0x01, 0x00, 0x00, 0x30, 0x01, 0x00, 0x00, 0x30, 
  0x01, 0x00, 0x00, 0x30, 0x01, 0x00, 0x00, 0x30, 0x01, 0x00, 0x00, 0x30, 
  0xFF, 0xFF, 0xFF, 0x3F, 0xFF, 0xFF, 0xFF, 0x3F
};
"""

RIGHTCLICKDOWN = """
#define rightclickdown_width 30
#define rightclickdown_height 20
static const unsigned char rightclickdown_bits[] = {
  0xFF, 0xFF, 0x03, 0x00, 0xFF, 0xFF, 0x1F, 0x00, 0xFF, 0xFF, 0x7F, 0x00, 
  0xFF, 0xFF, 0xFF, 0x00, 0xFF, 0xFF, 0xFF, 0x01, 0xFF, 0xFF, 0xFF, 0x03, 
  0xFF, 0xFF, 0xFF, 0x07, 0xFF, 0xFF, 0xFF, 0x0F, 0xFF, 0xFF, 0xFF, 0x0F, 
  0xFF, 0xFF, 0xFF, 0x1F, 0xFF, 0xFF, 0xFF, 0x1F, 0xFF, 0xFF, 0xFF, 0x3F, 
  0xFF, 0xFF, 0xFF, 0x3F, 0xFF, 0xFF, 0xFF, 0x3F, 0xFF, 0xFF, 0xFF, 0x3F, 
  0xFF, 0xFF, 0xFF, 0x3F, 0xFF, 0xFF, 0xFF, 0x3F, 0xFF, 0xFF, 0xFF, 0x3F, 
  0xFF, 0xFF, 0xFF, 0x3F, 0xFF, 0xFF, 0xFF, 0x3F
};
"""

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
        self.sliderTime=0
        self.running = 0
        self.leftclick = 0
        self.middleclick = 0
        self.rightclick = 0
                
        self.parent.overrideredirect(True)
        self.style = Style()
        self.style.theme_use("default")
        self.parent.wm_attributes("-topmost", 1)
        self.parent.resizable(0,0)
        
        self.gripBar = BitmapImage(data=GRIPBAR)
        self.closeBox = BitmapImage(data=CLOSEBOX)
        self.closeHover = BitmapImage(data=CLOSEHOVER)
        self.leftClick = BitmapImage(data=LEFTCLICK)
        self.leftClickDown = BitmapImage(data=LEFTCLICKDOWN)
        self.middleClick = BitmapImage(data=MIDDLECLICK)
        self.middleClickDown = BitmapImage(data=MIDDLECLICKDOWN)
        self.rightClick = BitmapImage(data=RIGHTCLICK)
        self.rightClickDown = BitmapImage(data=RIGHTCLICKDOWN)
        
        self.barFrame = Frame(self)
        self.barFrame.pack(side=TOP, fill=BOTH)
        self.clickFrame = Frame(self, borderwidth=0)
        self.clickFrame.pack(side=TOP, fill=BOTH, padx=12, expand=1)

        self.sliderScale = Scale(self, from_=0, to=1, resolution=.01, orient=HORIZONTAL, borderwidth=0, showvalue=0)
        self.sliderScale.pack(side=TOP, fill="x", expand=1)
        
        self.buttonFrame = Frame(self, borderwidth=0)
        self.buttonFrame.pack(side=TOP, fill=BOTH, expand=1)
        
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
        
        self.leftClickToggle = Label(self.clickFrame, image=self.leftClick, borderwidth=0)
        self.leftClickToggle.image=self.leftClick
        self.leftClickToggle.pack(side=LEFT, expand=1)
        self.leftClickToggle.bind("<Button-1>", self.leftToggle)
        
        self.middleClickToggle = Label(self.clickFrame, image=self.middleClick, borderwidth=0)
        self.middleClickToggle.image=self.middleClick
        self.middleClickToggle.pack(side=LEFT, expand=1)
        self.middleClickToggle.bind("<Button-1>", self.middleToggle)

        self.rightClickToggle = Label(self.clickFrame, image=self.rightClick, borderwidth=0)
        self.rightClickToggle.image=self.rightClick
        self.rightClickToggle.pack(side=LEFT, expand=1)
        self.rightClickToggle.bind("<Button-1>", self.rightToggle)

        self.startButton = Button(self.buttonFrame, text="Start (F2)", relief=FLAT, activebackground="lightgrey", borderwidth=0)
        self.startButton.pack(fill=BOTH, expand=1)
        self.startButton.bind("<Button-1>", self.startClick)
        self.startButton.bind("<<hotkey>>", self.startClick)
                
        self.w = 116
        self.h = 74

        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen

        x = (ws/2) - (self.w/2)
        y = (hs/2) - (self.h/2)

        self.parent.geometry('%dx%d+%d+%d' % (self.w, self.h, x, y))
        self.parent.config(bg="black")
        self.pack(fill="both", padx=1, pady=1)
        
        self.hk = SystemHotkey()
        self.hk.register(('f2',), callback=self.callBack)
            
    def callBack(self, event):
        self.startButton.event_generate("<<hotkey>>", when="tail")
        
    def leftToggle(self,event):
        if self.running == 0:
            if self.leftclick == 0:
                event.widget.configure(image=self.leftClickDown)
                self.leftclick = 1;
            else:
                event.widget.configure(image=self.leftClick)
                self.leftclick = 0;
                
    def middleToggle(self,event):
        if self.running == 0:
            if self.middleclick == 0:
                event.widget.configure(image=self.middleClickDown)
                self.middleclick = 1;
            else:
                event.widget.configure(image=self.middleClick)
                self.middleclick = 0;
                
    def rightToggle(self,event):
        if self.running == 0:
            if self.rightclick == 0:
                event.widget.configure(image=self.rightClickDown)
                self.rightclick = 1;
            else:
                event.widget.configure(image=self.rightClick)
                self.rightclick = 0;

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
        self.running = 0
        sys.exit()
            
    def startClick(self, event):
        if self.running == 0 and not (self.leftclick == 0 and self.middleclick==0 and self.rightclick == 0):
            self.running = 1
            event.widget.config(text="Stop (F2)")
            x = self.parent.winfo_x() + (self.w / 2)
            y = self.parent.winfo_y() + self.h + 50
            pyautogui.moveTo(x, y)
            threading.Thread(target=self.startLoop, args=()).start()
        else:
            self.running = 0
            event.widget.config(text="Start (F2)")
        time.sleep(0.2)
        return

    def startLoop(self):
        while self.running == 1:
            if self.leftclick == 1:
                pyautogui.click()
            if self.middleclick == 1:
                pyautogui.click(button="middle")
            if self.rightclick == 1:
                pyautogui.click(button="right")
            delay = self.sliderScale.get()
            time.sleep(delay)
        return
    
def main():
    root = Tk()
    app = autoClicker(root)
    root.mainloop()

if __name__ == "__main__":
    main() 
