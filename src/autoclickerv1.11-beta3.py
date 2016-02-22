#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyautogui, time, threading, sys
from tkinter import *
from system_hotkey import SystemHotkey
import tkinter as tk

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
        self.parent.wm_attributes("-topmost", 1)
        self.parent.resizable(0,0)
        
        self.gripBar = tk.PhotoImage(file='resources/bar.png')
        self.closeBox = tk.PhotoImage(file='resources/close.png')
        self.closeHover = tk.PhotoImage(file='resources/closehover.png')
        self.leftClick = tk.PhotoImage(file='resources/leftclick.png')
        self.leftClickDown = tk.PhotoImage(file='resources/leftclickdown.png')
        self.middleClick = tk.PhotoImage(file='resources/middleclick.png')
        self.middleClickDown = tk.PhotoImage(file='resources/middleclickdown.png')
        self.rightClick = tk.PhotoImage(file='resources/rightclick.png')
        self.rightClickDown = tk.PhotoImage(file='resources/rightclickdown.png')
        
        self.barFrame = Frame(self)
        self.barFrame.pack(side=TOP, fill=BOTH, pady="1")
        self.clickFrame = Frame(self, borderwidth=0, bg='white')
        self.clickFrame.pack(side=TOP, fill=BOTH, padx=12, expand=1)

        self.sliderScale = Scale(self, from_=0, to=1, resolution=.01, orient=HORIZONTAL, borderwidth=0, showvalue=0)
        self.sliderScale.pack(side=TOP, fill="x", expand=1)
        
        self.buttonFrame = Frame(self, borderwidth=0)
        self.buttonFrame.pack(side=TOP, fill=BOTH, expand=1)
        
        self.grip = tk.Label(self.barFrame, image=self.gripBar, borderwidth=0)
        self.grip.pack(side=LEFT, fill="x", padx=(1,0))
        self.grip.bind("<ButtonPress-1>", self.startMove)
        self.grip.bind("<ButtonRelease-1>", self.stopMove)
        self.grip.bind("<B1-Motion>", self.onMotion)
        
        self.closeButton = tk.Label(self.barFrame, image=self.closeBox, borderwidth=0)
        self.closeButton.pack(side=LEFT, fill="x", padx="1")
        self.closeButton.bind("<ButtonPress-1>", self.sysExit)
        self.closeButton.bind("<Enter>", self.onHover)
        self.closeButton.bind("<Leave>", self.onLeave)
        
        self.leftClickToggle = tk.Label(self.clickFrame, image=self.leftClick, borderwidth=0)
        self.leftClickToggle.pack(side=LEFT, expand=1)
        self.leftClickToggle.bind("<Button-1>", self.leftToggle)
        
        self.middleClickToggle = tk.Label(self.clickFrame, image=self.middleClick, borderwidth=0)
        self.middleClickToggle.pack(side=LEFT, expand=1)
        self.middleClickToggle.bind("<Button-1>", self.middleToggle)

        self.rightClickToggle = tk.Label(self.clickFrame, image=self.rightClick, borderwidth=0)
        self.rightClickToggle.pack(side=LEFT, expand=1)
        self.rightClickToggle.bind("<Button-1>", self.rightToggle)

        self.startButton = Button(self.buttonFrame, text="Start (F2)", relief=FLAT, activebackground="lightgrey", borderwidth=0)
        self.startButton.pack(fill=BOTH, expand=1)
        self.startButton.bind("<Button-1>", self.startClick)
        self.startButton.bind("<<hotkey>>", self.startClick)
                
        self.w = 115
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
