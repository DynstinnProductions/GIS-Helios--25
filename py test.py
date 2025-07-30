
import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("FocusZen")
root.configure(bg="#121212")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f"{width}x{height}")

MAIN_COLOR = "#a3aef7"
TEXT_COLOR = "#ffffff"
ACCENT_COLOR = "#aaaaaa"
FONT_HEADING = ("SF Pro Display", 52, "bold")
FONT_TIMER = ("SF Pro Display", 90)
FONT_SMALL = ("SF Pro Display", 14)
FONT_MEDIUM = ("SF Pro Display", 20)
FONT_LABEL = ("SF Pro Display", 18)

button_style = {
    "font": ("SF Pro Display", 18, "bold"),
    "fg": "#121212",
    "bg": MAIN_COLOR,
    "activebackground": "#00ccaa",
    "activeforeground": "#00A6FF",
    "bd": 0,
    "relief": "flat",
    "padx": 25,
    "pady": 12
}

current_time = tk.Label(root, font=FONT_SMALL, fg=ACCENT_COLOR, bg="#121212")
current_time.place(x=20, y=10)

heading = tk.Label(root, text="FocusZen", font=FONT_HEADING, fg=MAIN_COLOR, bg="#121212")
heading.pack(pady=(60, 30))

timer_label = tk.Label(root, text="25:00", font=FONT_TIMER, fg=TEXT_COLOR, bg="#121212")
timer_label.pack(pady=20)

result_label = tk.Label(root, font=FONT_LABEL, fg=ACCENT_COLOR, bg="#121212")
result_label.pack(pady=20)

button_frame = tk.Frame(root, bg="#121212")
button_frame.pack(pady=30)

start_button = tk.Button(button_frame, text="▶ Start", command=lambda: start_timer(), **button_style)
start_button.pack(side="left", padx=15)

stop_button = tk.Button(button_frame, text="⏹ Stop", command=lambda: stop_timer(), **button_style)
stop_button.pack(side="left", padx=15)

work_duration = 25 * 60
break_duration = 5 * 60
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
        result_label.config(text="Pomodoro started. Stay focused.")
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

def show_current_time():
    current_datetime = datetime.now().strftime("%H:%M")
    current_time.config(text=f"Time: {current_datetime}")
    root.after(1000, show_current_time)

show_current_time()
root.mainloop()