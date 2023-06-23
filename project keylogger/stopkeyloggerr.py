



# defining the function to perform operation on each key release 


import subprocess 
import keyword
from multiprocessing.connection import Listener
import tkinter
from tkinter.tix import WINDOW

from copykeyloggercode import functionPerKey

# Create a frame to hold the buttons
button_frame = tkinter.Frame(WINDOW)
button_frame.pack(expand=True)

def stop_keylogger():
    # Replace the command below with the actual command to stop your keylogger program
    subprocess.Popen(["python", "stopkeyloggerr.py"])
# Create the Stop button
stop_button = tkinter.Tk.Button(button_frame, text="Stop Keylogger", command=stop_keylogger)
def onEachKeyRelease(the_key):  
    # In case, the key is "Esc" then stopping the keylogger  
    if the_key == stop_button.stopkeylogger:  
        return False  
    
    
 