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
        
        self.gripBar = tk.PhotoImage(file=resource_path('resources/bar.png'))
        self.closeBox = tk.PhotoImage(file=resource_path('resources/close.png'))
        self.closeHover = tk.PhotoImage(file=resource_path('resources/closehover.png'))
        self.leftClick = tk.PhotoImage(file=resource_path('resources/leftclick.png'))
        self.leftClickDown = tk.PhotoImage(file=resource_path('resources/leftclickdown.png'))
        self.middleClick = tk.PhotoImage(file=resource_path('resources/middleclick.png'))
        self.middleClickDown = tk.PhotoImage(file=resource_path('resources/middleclickdown.png'))
        self.rightClick = tk.PhotoImage(file=resource_path('resources/rightclick.png'))
        self.rightClickDown = tk.PhotoImage(file=resource_path('resources/rightclickdown.png'))
        self.runningImg = tk.PhotoImage(file=resource_path('resources/running.png'))
        self.stoppedImg = tk.PhotoImage(file=resource_path('resources/stopped.png'))
        self.ledOff = tk.PhotoImage(file=resource_path('resources/ledoff.png'))
        
        self.barFrame = Frame(self, borderwidth=0)
        self.barFrame.pack(side=TOP, fill=BOTH, pady=1, expand=1)
        
        self.clickFrame = Frame(self, borderwidth=0)
        self.clickFrame.pack(side=TOP, fill=BOTH, padx=(6,3), expand=1)
        
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
        self.leftClickToggle.pack(side=LEFT, expand=1, pady=(2,1))
        self.leftClickToggle.bind("<Button-1>", self.leftToggle)
        
        self.middleClickToggle = tk.Label(self.clickFrame, image=self.middleClick, borderwidth=0)
        self.middleClickToggle.pack(side=LEFT, expand=1, pady=(2,1))
        self.middleClickToggle.bind("<Button-1>", self.middleToggle)

        self.rightClickToggle = tk.Label(self.clickFrame, image=self.rightClick, borderwidth=0)
        self.rightClickToggle.pack(side=LEFT, expand=1, pady=(2,1))
        self.rightClickToggle.bind("<Button-1>", self.rightToggle)
        
        self.statusFrame = Frame(self.clickFrame, borderwidth=0)
        self.statusFrame.pack(side=LEFT, fill=BOTH, expand=1)

        self.statusLabel = tk.Label(self.statusFrame, image=self.ledOff, borderwidth=0)
        self.statusLabel.pack(side=TOP, fill=BOTH, padx=(3,0), pady=(0,1))
        
        self.statusLabel.bind("<<hotkey>>", self.startClick)
        
        self.statusLabel2 = tk.Label(self.statusFrame, image=self.stoppedImg, borderwidth=0)
        self.statusLabel2.pack(side=TOP, fill=BOTH, padx=(3,0), pady=1)
                
        self.w = 115
        self.h = 37

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
        self.statusLabel.event_generate("<<hotkey>>", when="tail")
        
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
            event.widget.configure(image=self.runningImg)
            self.statusLabel2.configure(image=self.ledOff)
            threading.Thread(target=self.startLoop, args=()).start()
        else:
            self.running = 0
            event.widget.configure(image=self.ledOff)
            self.statusLabel2.configure(image=self.stoppedImg)
            
        return

    def startLoop(self):
        while self.running == 1:
            if self.leftclick == 1:
                pyautogui.click()
            if self.middleclick == 1:
                pyautogui.click(button="middle")
            if self.rightclick == 1:
                pyautogui.click(button="right")
        return
    
def main():
    root = Tk()
    app = autoClicker(root)
    root.mainloop()
    
def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )

if __name__ == "__main__":
    main() 
