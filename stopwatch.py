import tkinter as Tkinter
from datetime import datetime

counter = 66600
running = False
laps = []

def counter_label(label):
    def count():
        global counter
        if running:
            display = "Starting..." if counter == 66600 else datetime.fromtimestamp(counter).strftime("%H:%M:%S")
            label.config(text=display)
            label.after(1000, count)
            counter += 1
    count()

def start_timer(label):
    global running
    running = True
    counter_label(label)
    start_btn.config(state='disabled')
    stop_btn.config(state='normal')
    reset_btn.config(state='normal')
    lap_btn.config(state='normal')
    label.config(fg="#006400")  # Dark green

def stop_timer():
    global running
    running = False
    start_btn.config(state='normal')
    stop_btn.config(state='disabled')
    lap_btn.config(state='disabled')
    label.config(fg="#8B0000")  # Dark red

def reset_timer(label):
    global counter, laps
    counter = 66600
    laps = []  # Clear laps
    label.config(text='Welcome!' if not running else 'Starting...', fg="#000000")  # Black
    reset_btn.config(state='disabled' if not running else 'normal')
    laps_list.config(state='normal')
    laps_list.delete(1.0, Tkinter.END)
    laps_list.config(state='disabled')

def lap_timer():
    global counter
    if running:
        lap_time = datetime.fromtimestamp(counter - 66600).strftime("%H:%M:%S")
        laps.append(lap_time)
        laps_list.config(state='normal')
        laps_list.insert(Tkinter.END, f"Lap {len(laps)}: {lap_time}\n")
        laps_list.config(state='disabled')
    else:
        laps_list.config(state='normal')
        laps_list.insert(Tkinter.END, "Start the timer to record laps.\n")
        laps_list.config(state='disabled')

root = Tkinter.Tk()
root.title("Stopwatch")
root.geometry("350x400")
root.configure(bg='#ADD8E6')  # Light blue background color for the root window

label = Tkinter.Label(root, text="Welcome!", fg="white", bg="#ADD8E6", font="Verdana 30 bold")
label.pack(pady=20)

frame = Tkinter.Frame(root, bg='#87CEFA')  # Light sky blue background for the frame
start_btn = Tkinter.Button(frame, text='Start', width=6, command=lambda: start_timer(label), bg='#4CAF50', fg='white')  # Green
stop_btn = Tkinter.Button(frame, text='Stop', width=6, state='disabled', command=stop_timer, bg='#F44336', fg='white')  # Red
reset_btn = Tkinter.Button(frame, text='Reset', width=6, state='disabled', command=lambda: reset_timer(label), bg='#2196F3', fg='white')  # Blue
lap_btn = Tkinter.Button(frame, text='Lap', width=6, state='disabled', command=lap_timer, bg='#FFC107', fg='white')  # Amber

frame.pack(anchor='center', pady=5)
start_btn.pack(side="left", padx=5)
stop_btn.pack(side="left", padx=5)
reset_btn.pack(side="left", padx=5)
lap_btn.pack(side="left", padx=5)

laps_list = Tkinter.Text(root, width=35, height=10, state='disabled', bg='#B0C4DE', fg='black', font=('Arial', 10))  # Light steel blue background
laps_list.pack(pady=10)

root.mainloop()
