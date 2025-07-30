import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("FocusZen")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f"{width}x{height}")

heading = tk.Label(root, text="Pomodoro Timer", font=("San Francisco", 48), fg="black")
heading.pack(ipady=5)

current_time = tk.Label(root, font=("San Francisco", 24), fg="black")
current_time.pack(pady=20)

timer_label = tk.Label(root, text="25:00", font=("San Francisco", 72), fg="black")
timer_label.pack(pady=20)

result_label = tk.Label(root, font=("San Francisco", 20), fg="black")
result_label.pack(pady=20)

work_duration = 0.1 * 60
break_duration = 0.2 * 60
timer_running = False
timer_id = None

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


start_button = tk.Button(root, text="Start Pomodoro", command=start_timer, font=("Helvetica", 24), fg="black")
start_button.pack(pady=20)

stop_button = tk.Button(root, text="Stop Pomodoro", command=stop_timer, font=("Helvetica", 24), fg="black")
stop_button.pack(pady=20)

def show_current_time():
    current_datetime = datetime.now().strftime("%H:%M")
    current_time.config(text=f"Current Time : {current_datetime}")
    root.after(1000, show_current_time)

show_current_time()

root.mainloop()