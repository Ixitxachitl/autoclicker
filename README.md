# autoclicker

Usage:
  1) Click on the mouse buttons you'd like to auto click
  2) (Optional) Move mouse to where you'd like to click and define the area with F7
  3) Press F2 to begin clicking
  4) (Optional) Press F8 to return to defined area

Designed to click on cookies: http://orteil.dashnet.org/cookieclicker/

You can also run the script directly:
>>>python3 autoclick\<version\>.py

Requirements:

  Windows:
  
            Python for Windows:
            (I used python 3.5 but any version of python 3.x should work)
            https://www.python.org/downloads/
  
            Tcl/tk for Windows: 
            http://www.activestate.com/activetcl/downloads
            
            pywin32:
            (make sure you install the version that maches the version of python that you have installed)
            https://sourceforge.net/projects/pywin32/
            
            PyAutoGui:
            c:\path\to\pip install pillow
            c:\path\to\pip install pyautogui
            
            System_Hotkey
            c:\path\to\pip install system_hotkey
            + any required modules
  
  Ubuntu:
  
            Python 3:
            sudo apt-get install python3.5
            
            Python tk:
            sudo apt-get install python3-tk
            
            Pip 3:
            sudo apt-get install python3-pip
            
            PyAutoGui:
            pip3 install pillow
            pip3 install pyautogui
            pip3 install system_hotkey
            + any required modules
            
Mac OS users: Newest version uses system_hotkey modual that does not currently support Mac OS, the script will run but without keybindings the current version cannot start and will require a workaround.
