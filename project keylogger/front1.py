import tkinter as tk
import subprocess

def start_keylogger():
    # Replace the command below with the actual command to start your keylogger program
    subprocess.Popen(["python", "keylogger.py"])

def stop_keylogger():
    # Replace the command below with the actual command to stop your keylogger program
    subprocess.Popen(["python", "topkeyloggerr.py"])

# Create the GUI window
window = tk.Tk()
window.title('Keylogger Page')
window.geometry("300x200+10+20")
lbl=tk.Label(window, text="WELCOME TO KEYLOGGER PAGE", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)

# Create a frame to hold the buttons
button_frame = tk.Frame(window)
button_frame.pack(expand=True)

# Create the Start button
start_button = tk.Button(button_frame, text="Start Keylogger", command=start_keylogger)
start_button.pack(side='left', padx=10, pady=10)

# Create the Stop button
stop_button = tk.Button(button_frame, text="Stop Keylogger", command=stop_keylogger)
stop_button.pack(side='right', padx=10, pady=10)

# Run the GUI window
window.mainloop()
