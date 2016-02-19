# autoclicker

Download Executable and click Start to start clicking, move your mouse over Stop to stop.
Note: Current version clicks left mouse button and than middle mouse button and after a (very) short dely repeats until the start/stop button or close button is pressed.

Designed to click on cookies: http://orteil.dashnet.org/cookieclicker/

You can also run the script directly:
>>>python3 autoclick.py

Requirements:

  Windows:
  
            Python for Windows:
            (I used python 3.5 but any version of python 3.x should work or 2.x with some minor changes)
            https://www.python.org/downloads/
  
            Tcl/tk for Windows: 
            http://www.activestate.com/activetcl/downloads
            
            pywin32:
            (make sure you install the version that maches the version of python that you have installed)
            https://sourceforge.net/projects/pywin32/
            
            PyAutoGui:
            c:\path\to\pip install pillow
            c:\path\to\pip install pyautogui
  
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
            
Mac OS users: You can run this script directly by installing python 3.x, tkinter modual and pyautogui but as I do not have an osx device I am unable to pre-compile this for you and do not have detailed instructions.  That being said, I'm sure the instalation process is pretty strait forward and if someone with an osx device is willing to step forward i'd be happy to have someone compile it for me.  Because pyinstaller is not a cross compiler, in order to have an osx executable it must be compiled on the target device or a virtual environment such as the way I compile the windows executable using wine.
If you notice any errors in my instalation process or have any tips let me know and I'll fix it, Thanks!
