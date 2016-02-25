#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyautogui, time, threading, sys, os, logging
from tkinter import *
from system_hotkey import SystemHotkey
import tkinter as tk

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s',)

class autoClicker(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.topFrame1 = Toplevel()
        self.topFrame1.overrideredirect(True)
        self.topFrame1.config(bg="red", bd=0, height=2, width=50)
        self.topFrame1.withdraw()
        self.topFrame2 = Toplevel()
        self.topFrame2.overrideredirect(True)
        self.topFrame2.config(bg="red", bd=0, height=50, width=2)
        self.topFrame2.withdraw()
        self.topFrame3 = Toplevel()
        self.topFrame3.overrideredirect(True)
        self.topFrame3.config(bg="red", bd=0, height=2, width=50)
        self.topFrame3.withdraw()
        self.topFrame4 = Toplevel()
        self.topFrame4.overrideredirect(True)
        self.topFrame4.config(bg="red", bd=0, height=50, width=2)
        self.topFrame4.withdraw()
        
        self.running = 0
        self.leftclick = 0
        self.middleclick = 0
        self.rightclick = 0
        self.systemStart = 1
        self.spotx = 0
        self.spoty = 0
        self.lastspotx = 0
        self.lastspoty = 0
        self.flagReturn = 0
                
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
        
        self.goldCookie1 = resource_path('resources/goldCookie1.png')
        self.goldCookie2 = resource_path('resources/goldCookie2.png')
        self.goldCookie3 = resource_path('resources/goldCookie3.png')
        self.goldCookie4 = resource_path('resources/goldCookie4.png')
        
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
        
        self.registerHotkeys()
                
    def registerHotkeys(self):
        logging.debug("Binding Keys:")
        self.hk = SystemHotkey()
        try:
            self.hk.register(('f2',), callback=self.callBack)
            logging.debug(" f2 bound")
        except:
            logging.debug(" Bind Failed: Continuing...")
        try:
            self.hk.register(('o',), callback=self.setSpot)
            logging.debug(" o bound")
        except:
            logging.debug(" Bind Failed: Continuing...")
        try:
            self.hk.register(('p',), callback=self.returnSpot)
            logging.debug(" p bound")
        except:
            logging.debug(" Bind Failed: Continuing...")
        return
        
    def setSpot(self, event):
        if not self.running == 1:
            logging.debug("<<!!Spot Call!!>>")
            logging.debug("spotx: %d -- %s", self.spotx, self.lastspotx)
            logging.debug("spoty: %d -- %s", self.spoty, self.lastspoty)
            if self.spotx == 0 and self.spoty == 0:
                self.lastspotx = 0
                self.lastspoty = 0            
            self.spotx, self.spoty = pyautogui.position()
            if self.spotx == self.lastspotx and self.spoty == self.lastspoty:
                logging.debug("--Spot Reset--")
                logging.debug("spotx: %d -- %s", self.spotx, self.lastspotx)
                logging.debug("spoty: %d -- %s", self.spoty, self.lastspoty)
                self.lastspotx = self.spotx
                self.lastspoty = self.spoty
                self.spotx = 0
                self.spoty = 0               
                self.topFrame1.withdraw()
                self.topFrame2.withdraw()
                self.topFrame3.withdraw()
                self.topFrame4.withdraw()
            else:
                logging.debug("--Spot Move--")
                logging.debug("spotx: %d -- %s", self.spotx, self.lastspotx)
                logging.debug("spoty: %d -- %s", self.spoty, self.lastspoty)
                self.lastspotx = self.spotx
                self.lastspoty = self.spoty
                self.topFrame1.geometry('50x2+%d+%d' % (self.spotx - 25, self.spoty - 25))
                self.topFrame2.geometry('2x50+%d+%d' % (self.spotx - 25, self.spoty - 25))
                self.topFrame3.geometry('52x2+%d+%d' % (self.spotx - 25, self.spoty + 25))
                self.topFrame4.geometry('2x50+%d+%d' % (self.spotx + 23, self.spoty - 25))
                self.topFrame1.deiconify()
                self.topFrame2.deiconify()
                self.topFrame3.deiconify()
                self.topFrame4.deiconify()
        return
                
    def returnSpot(self, event):
        if not (self.spotx == 0 and self.spoty == 0):
            if not (self.running == 1):
                pyautogui.moveTo(self.spotx, self.spoty)
            else:
                self.flagReturn = 1
                
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
        self.systemStart = 0
        sys.exit()
            
    def startClick(self, event):
        if self.running == 0 and not (self.leftclick == 0 and self.middleclick==0 and self.rightclick == 0):
            self.running = 1
            logging.debug("Started")
            event.widget.configure(image=self.runningImg)
            self.statusLabel2.configure(image=self.ledOff)
            threading.Thread(target=self.startLoop, args=()).start()
        else:
            self.running = 0
            logging.debug("Stopped")
            event.widget.configure(image=self.ledOff)
            self.statusLabel2.configure(image=self.stoppedImg)
        return

    def startLoop(self):
        logging.debug("spotx: %s", self.spotx)
        logging.debug("spoty: %s", self.spoty)
        while self.running == 1:
            if self.spotx == 0 and self.spoty == 0:
                if self.leftclick == 1:
                    pyautogui.click()
                if self.middleclick == 1:
                    pyautogui.click(button="middle")
                if self.rightclick == 1:
                    pyautogui.click(button="right")
            elif not(self.spotx == 0 and self.spoty == 0):
                self.positionX, self.positionY = pyautogui.position()
                self.upperX = self.spotx + 25
                self.lowerX = self.spotx - 25
                self.upperY = self.spoty + 25
                self.lowerY = self.spoty - 25
                if (self.lowerX < self.positionX < self.upperX) and (self.lowerY < self.positionY < self.upperY):
                    if self.leftclick == 1:
                        pyautogui.click()
                    if self.middleclick == 1:
                        pyautogui.click(button="middle")
                    if self.rightclick == 1:
                        pyautogui.click(button="right")
            if self.flagReturn == 1:
                pyautogui.moveTo(self.spotx, self.spoty)
                self.flagReturn = 0
        return

def main():
    root = Tk()
    app = autoClicker(root)
    root.mainloop()
    
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    main() 
