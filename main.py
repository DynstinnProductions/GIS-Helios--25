# FocuZen - A Minimalist Focus Timer which shows a timer in the midde and is like full screen app which can help you to focus on your work and also has a area where your spotify playlist can be embedded through entering the playlist name
#it also sets a pomodoro timer for 25 minutes and then gives a break of 5 minutes
#it also has a small task reminder

'''
('System', 'Terminal', 'Fixedsys', 'Modern', 'Roman', 'Script', 'Courier', 'MS Serif', 'MS Sans Serif', 'Small Fonts', '8514oem', 
'Marlett', 'Arial', 'Arabic Transparent', 'Arial Baltic', 'Arial CE', 'Arial CYR', 'Arial Greek', 'Arial TUR', 'Arial Black', 'Bahnschrift Light', 
'Bahnschrift SemiLight', 'Bahnschrift', 'Bahnschrift SemiBold', 'Bahnschrift Light SemiCondensed', 'Bahnschrift SemiLight SemiConde',
'Bahnschrift SemiCondensed', 'Bahnschrift SemiBold SemiConden', 'Bahnschrift Light Condensed', 'Bahnschrift SemiLight Condensed', 'Bahnschrift Condensed',
'Bahnschrift SemiBold Condensed', 'Calibri', 'Calibri Light', 'Cambria', 'Cambria Math', 'Candara', 'Candara Light', 'Comic Sans MS', 'Consolas', 'Constantia',
'Corbel', 'Corbel Light', 'Courier New', 'Courier New Baltic', 'Courier New CE', 'Courier New CYR', 'Courier New Greek', 'Courier New TUR', 'Ebrima', 'Franklin Gothic Medium',
'Gabriola', 'Gadugi', 'Georgia', 'Impact', 'Ink Free', 'Javanese Text', 'Leelawadee UI', 'Leelawadee UI Semilight', 'Lucida Console', 'Lucida Sans Unicode', 'Malgun Gothic',
'@Malgun Gothic', 'Malgun Gothic Semilight', '@Malgun Gothic Semilight', 'Microsoft Himalaya', 'Microsoft JhengHei', '@Microsoft JhengHei', 'Microsoft JhengHei UI',
'@Microsoft JhengHei UI', 'Microsoft JhengHei Light', '@Microsoft JhengHei Light', 'Microsoft JhengHei UI Light', '@Microsoft JhengHei UI Light', 'Microsoft New Tai Lue',
'Microsoft PhagsPa', 'Microsoft Sans Serif', 'Microsoft Tai Le', 'Microsoft YaHei', '@Microsoft YaHei', 'Microsoft YaHei UI', '@Microsoft YaHei UI', 'Microsoft YaHei Light',
'@Microsoft YaHei Light', 'Microsoft YaHei UI Light', '@Microsoft YaHei UI Light', 'Microsoft Yi Baiti', 'MingLiU-ExtB', '@MingLiU-ExtB', 'PMingLiU-ExtB', '@PMingLiU-ExtB',
'MingLiU_HKSCS-ExtB', '@MingLiU_HKSCS-ExtB', 'MingLiU_MSCS-ExtB', '@MingLiU_MSCS-ExtB', 'Mongolian Baiti', 'MS Gothic', '@MS Gothic', 'MS UI Gothic', '@MS UI Gothic',
'MS PGothic', '@MS PGothic', 'MV Boli', 'Myanmar Text', 'Nirmala UI', 'Nirmala UI Semilight', 'Nirmala Text', 'Nirmala Text Semilight', 'Palatino Linotype',
'Sans Serif Collection', 'Segoe Fluent Icons', 'Segoe MDL2 Assets', 'Segoe Print', 'Segoe Script', 'Segoe UI', 'Segoe UI Black', 'Segoe UI Emoji', 'Segoe UI Historic',
'Segoe UI Light', 'Segoe UI Semibold', 'Segoe UI Semilight', 'Segoe UI Symbol', 'Segoe UI Variable Small Light', 'Segoe UI Variable Small Semilig', 'Segoe UI Variable Small',
'Segoe UI Variable Small Semibol', 'Segoe UI Variable Text Light', 'Segoe UI Variable Text Semiligh', 'Segoe UI Variable Text', 'Segoe UI Variable Text Semibold',
'Segoe UI Variable Display Light', 'Segoe UI Variable Display Semil', 'Segoe UI Variable Display', 'Segoe UI Variable Display Semib', 'SimSun', '@SimSun', 'NSimSun',
'@NSimSun', 'SimSun-ExtB', '@SimSun-ExtB', 'Sitka Small', 'Sitka Small Semibold', 'Sitka Text', 'Sitka Text Semibold', 'Sitka Subheading', 'Sitka Subheading Semibold',
'Sitka Heading', 'Sitka Heading Semibold', 'Sitka Display', 'Sitka Display Semibold', 'Sitka Banner', 'Sitka Banner Semibold', 'Sylfaen', 'Symbol', 'Tahoma', 'Times New Roman',
'Times New Roman Baltic', 'Times New Roman CE', 'Times New Roman CYR', 'Times New Roman Greek', 'Times New Roman TUR', 'Trebuchet MS', 'Verdana', 'Webdings', 'Wingdings',
'Yu Gothic', '@Yu Gothic', 'Yu Gothic UI', '@Yu Gothic UI', 'Yu Gothic UI Semibold', '@Yu Gothic UI Semibold', 'Yu Gothic Light', '@Yu Gothic Light', 'Yu Gothic UI Light',
'@Yu Gothic UI Light', 'Yu Gothic Medium', '@Yu Gothic Medium', 'Yu Gothic UI Semilight', '@Yu Gothic UI Semilight', 'SimSun-ExtG', '@SimSun-ExtG', 'Cascadia Code ExtraLight',
'Cascadia Code Light', 'Cascadia Code SemiLight', 'Cascadia Code', 'Cascadia Code SemiBold', 'Cascadia Mono ExtraLight', 'Cascadia Mono Light', 'Cascadia Mono SemiLight',
'Cascadia Mono', 'Cascadia Mono SemiBold', 'AKG Verdana', 'Arial Narrow', 'Crown SA', 'Crown SA Tight', 'Estrangelo Edessa', 'Unispace')
'''


import tkinter as tk 
from tkinter import messagebox
import time
import time
from time import gmtime, strftime, time
from datetime import datetime

time_left: float = 1500.00  # 25 minutes in seconds

root = tk.Tk()
root.title("FocusZen")
width =  root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f"{width}x{height}")

heading = tk.Label(root, text="Pomodoro Timer", font=("SF Pro", 48), fg="black")
heading.pack(ipady=5)
root.overrideredirect(True)

current_time = tk.Label(root, font=("SF Pro", 24), fg="black")
current_time.pack(pady=20, padx=20)

timer_label = tk.Label(root, text="25:00", font=("San Francisco", 72), fg="black")
timer_label.pack(pady=20)

result_label = tk.Label(root, font=("San Francisco", 20), fg="black")
result_label.pack(pady=20)

work_duration = 25 * 60
break_duration = 5 * 60
timer_running = False
timer_id = None

#pomodoro timer
def show_current_time():
    current_datetime = datetime.now().strftime("%H:%M")
    current_time.config(text=f"Current Time : {current_datetime}")
    root.after(600, show_current_time)  # Update every second

def countdown(seconds, is_break=False):
    global timer_id
    minutes, sec = divmod(seconds, 60)
    timer_label.config(text=f"{minutes:02}:{sec:02}")
    if seconds > 0:
        timer_id = root.after(1000, countdown, seconds - 1, is_break)
    else:
        if is_break:
            result_label.config(text="Break's over! Back to work.")
        else:
            result_label.config(text="Pomodoro done! Time for a 5-minute break.")
            start_break()

def start_timer():
    global timer_running
    if not timer_running:
        timer_running = True
        result_label.config(text="Pomodoro started. Stay focused!")
        countdown(work_duration)

def start_break():
    countdown(break_duration, is_break=True)

def stop_timer():
    global timer_id, timer_running
    if timer_id:
        root.after_cancel(timer_id)
        timer_running = False
        timer_label.config(text="25:00")
        result_label.config(text="Pomodoro stopped.")

start_button = tk.Button(root, text="Start Pomodoro", command=start_timer, font=("SF P", 24), fg="black")
start_button.pack(pady=20)

stop_button = tk.Button(root, text="Stop Pomodoro", command=stop_timer, font=("Helvetica", 24), fg="black")
stop_button.pack(pady=20)

def show_current_time():
    current_datetime = datetime.now().strftime("%H:%M")
    current_time.config(text=f"Current Time : {current_datetime}")
    root.after(1000, show_current_time)

show_current_time()

#GUI
root.mainloop()