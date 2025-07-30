import tkinter as tk
from tkinter import ttk
from datetime import datetime

root = tk.Tk()
root.title("FocusZen")
root.configure(bg="#000000")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f"{width}x{height}")
root.overrideredirect(True)

MAIN_COLOR = "#8cc9ea"
DARKER_MAIN = "#5da9cb"
TEXT_COLOR = "#ffffff"
ACCENT_COLOR = "#aaaaaa"
FONT_HEADING = ("Segoe UI", 28, "bold")
FONT_TIMER = ("San Frans", 180, "bold")
FONT_SMALL = ("Segoe UI", 12)
FONT_LABEL = ("Segoe UI", 17)
FONT_BUTTON = ("Segoe UI", 16, "bold")

style = ttk.Style()
style.theme_use("clam")
style.configure("Rounded.TButton", font=FONT_BUTTON, foreground="#121212", background=MAIN_COLOR, padding=10, borderwidth=0, focusthickness=0)
style.map("Rounded.TButton",background=[("active", DARKER_MAIN)])

current_time = tk.Label(root, font=FONT_SMALL, fg=ACCENT_COLOR, bg="#000000")
current_time.place(x=20, y=10)

heading = tk.Label(root, text="FocusZen", font=FONT_HEADING, fg=MAIN_COLOR, bg="#000000")
heading.place(x=width - 190, y=0)

timer_label = tk.Label(root, text="25:00", font=FONT_TIMER, fg=TEXT_COLOR, bg="#000000")
timer_label.place(relx=0.5, rely=0.35, anchor="center")

result_label = tk.Label(root, font=FONT_LABEL, fg=ACCENT_COLOR, bg="#000000")
result_label.place(relx=0.5, rely=0.55, anchor="center")

button_frame = tk.Frame(root, bg="#000000")
button_frame.place(relx=0.5, rely=0.65, anchor="center")

start_button = ttk.Button(button_frame, text="Start", command=lambda: start_timer(), style="Rounded.TButton")
start_button.pack(side="left", padx=15)

stop_button = ttk.Button(button_frame, text="Stop", command=lambda: stop_timer(), style="Rounded.TButton")
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