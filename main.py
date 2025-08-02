import tkinter as tk
from tkinter import ttk
from datetime import datetime

root = tk.Tk()
root.title("FocusZen")
root.configure(bg="#000000")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f"{width}x{height}")
#root.overrideredirect(True)

MAIN_COLOR = "#8cc9ea"
DARKER_MAIN = "#5da9cb"
TEXT_COLOR = "#ffffff"
ACCENT_COLOR = "#aaaaaa"
FONT_HEADING = ("Segoe UI", 28, "bold")
FONT_TIMER = ("San Frans", 180, "bold")
FONT_SMALL = ("Segoe UI", 12)
FONT_LABEL = ("Segoe UI", 15)
FONT_BUTTON = ("Segoe UI", 15, "bold")
CLOSE_BUTTON=("Segoe UI", 10,)
LISTBOX = ("Segoe UI", 12)
CLEAR_ALL = ("Segoe UI", 10)

style = ttk.Style()
style.theme_use("clam")
style.configure("Rounded.TButton", font=FONT_BUTTON, foreground="#121212", background=MAIN_COLOR, padding=10, borderwidth=0, focusthickness=0)
style.map("Rounded.TButton", background=[("active", DARKER_MAIN)])
style.configure(".TButton", font=FONT_HEADING, foreground="#121212", background=MAIN_COLOR, padding=10, borderwidth=0, focusthickness=0)
style.map(".TButton", background=[("active", DARKER_MAIN)])

current_time = tk.Label(root, font=FONT_SMALL, fg=ACCENT_COLOR, bg="#000000")
current_time.place(x=20, y=10)

heading = tk.Label(root, text="FocusZen", font=FONT_HEADING, fg=MAIN_COLOR, bg="#000000")
heading.place(x=1800, y=10, anchor="n")

button_frame = tk.Frame(root, bg="#000000")
button_frame.place(relx=0.5, rely=0.65, anchor="center")

result_label = tk.Label(root, font=FONT_LABEL, fg=ACCENT_COLOR, bg="#000000")
result_label.place(relx=0.5, rely=0.55, anchor="center")

input_frame = tk.Frame(root, bg="#000000")
input_frame.place(relx=0.5, rely=0.4, anchor="center")

label_style = {"font": FONT_LABEL, "fg": TEXT_COLOR, "bg": "#000000"}
entry_style = {"font": FONT_BUTTON, "fg": "#000000", "justify": "center", "width": 15, "relief": "flat"}

task_frame = tk.Frame(root, bg="#000000")
task_frame.place(x=1600, y=50, width=300, height=500)

task_label = tk.Label(task_frame, text="Task Reminder", font=FONT_LABEL, fg=MAIN_COLOR, bg="#000000")
task_label.place(x=10, y=10)

task_entry = tk.Entry(task_frame, font=FONT_BUTTON, fg="#000000", justify="left", width=20, relief="flat")
task_entry.place(x=10, y=50)

task_button = tk.Button(task_frame, text="Enter Task", font=FONT_BUTTON, fg="#000000", bg=MAIN_COLOR, command= lambda: task(), relief="flat")
task_button.place(x=10, y=100)

list_label = tk.Label(task_frame, text="Task List", font=FONT_LABEL, fg=MAIN_COLOR, bg="#000000")
list_label.place(x=10, y=150)

clear_all = tk.Button(task_frame, text="Clear All", font=CLEAR_ALL, fg=MAIN_COLOR, bg="#000000", command=lambda: task_listbox.delete(0, tk.END), relief="flat")
clear_all.place(x=10, y=200)

task_listbox = tk.Listbox(task_frame, font=LISTBOX, fg=MAIN_COLOR, bg="#000000", width=25, height=40, relief="flat")
task_listbox.place(x=10, y=230)



def task():
    task_text = task_entry.get()
    if task_text:
        task_listbox.insert(tk.END, task_text)
        task_entry.delete(0, tk.END)
    else:
        result_label.config(text="Please enter a task.")
    
    result_label.config(text="Task added to the list.")

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)
        result_label.config(text="Task deleted from the list.")
    else:
        result_label.config(text="Please select a task to delete.")



work_label = tk.Label(input_frame, text="Work Duration", **label_style)
work_duration_input = tk.Entry(input_frame, **entry_style)
break_label = tk.Label(input_frame, text="Break Duration", **label_style)
break_duration_input = tk.Entry(input_frame, **entry_style)

durations_push = ttk.Button(input_frame, text="Set Durations", command=lambda: get_durations(), style=".TButton")

work_label.pack(pady=(0, 5))
work_duration_input.pack(pady=(0, 15))
break_label.pack(pady=(0, 5))
break_duration_input.pack(pady=(0, 15))
durations_push.pack(pady=(10, 0))

back_button = ttk.Button(root, text="Back", command=lambda: go_back(), style="Rounded.TButton")

work_duration = 0
break_duration = 0

def get_durations():
    global work_duration, break_duration
    work_text = work_duration_input.get()
    break_text = break_duration_input.get()
    try:
        work_value = int(work_text)
        break_value = int(break_text)
    except ValueError:
        result_label.config(text="Please enter valid durations.")
        return
    break_duration = break_value * 60
    work_duration = work_value * 60
    verify_input()

def verify_input():
    global work_duration, break_duration
    if (work_duration <= 0 or break_duration <= 0 or type(work_duration) != int or type(break_duration) != int
            or work_duration_input.get() == "" or break_duration_input.get() == ""):
        result_label.config(text="Please enter valid durations.")
        return False
    result_label.config(text=f"Work Duration: {work_duration//60} minutes, Break Duration: {break_duration//60} minutes")
    input_frame.place_forget()
    back_button.place(x=20, y=60)
    result_label.config(text="Ready to start your Pomodoro session!")
    app_state_2()
    result_label.config(text="Press Start to begin your Pomodoro session.")
    return True

def go_back():
    work_duration_input.delete(0, 'end')
    break_duration_input.delete(0, 'end')
    restart_timer()
    timer_label.place_forget()
    start_button.pack_forget()
    pause_button.pack_forget()
    restart_button.pack_forget()
    back_button.place_forget()
    input_frame.place(relx=0.5, rely=0.4, anchor="center")
    result_label.config(text="")

timer_label = tk.Label(root, text=f"{work_duration:02}:00", font=FONT_TIMER, fg=TEXT_COLOR, bg="#000000")
start_button = ttk.Button(button_frame, text="Start", command=lambda: start_timer(), style="Rounded.TButton")
pause_button = ttk.Button(button_frame, text="Pause", command=lambda: pause_timer(), style="Rounded.TButton")
restart_button = ttk.Button(button_frame, text="Restart", command=lambda: restart_timer(), style="Rounded.TButton")

remaining_time = 0
is_on_break = False

def app_state_2():
    restart_timer()
    timer_label.place(relx=0.5, rely=0.35, anchor="center")
    start_button.pack(side="left", padx=15)
    pause_button.pack(side="left", padx=15)
    restart_button.pack(side="left", padx=15)

timer_running = False
timer_id = None

def countdown(seconds, is_break=False):
    global timer_id, remaining_time, is_on_break
    is_on_break = is_break
    remaining_time = seconds
    minutes, sec = divmod(seconds, 60)
    timer_label.config(text=f"{minutes:02}:{sec:02}")
    if seconds > 0:
        timer_id = root.after(1000, countdown, seconds - 1, is_break)
    else:
        if is_break:
            result_label.config(text="Break's over! Back to work.")
        else:
            result_label.config(text=f"Pomodoro done! Time for a {break_duration // 60}-minute break.")
            start_break()

def start_timer():
    global timer_running
    if not timer_running:
        timer_running = True
        result_label.config(text="Pomodoro started. Stay focused.")
        countdown(remaining_time if remaining_time > 0 else work_duration)

def start_break():
    countdown(break_duration, is_break=True)

def pause_timer():
    global timer_running, timer_id
    if timer_running and timer_id:
        root.after_cancel(timer_id)
        timer_running = False
        result_label.config(text="Timer paused.")

def restart_timer():
    global timer_running, timer_id, remaining_time, work_duration
    if timer_id:
        root.after_cancel(timer_id)
    timer_running = False
    remaining_time = 0
    minutes, sec = divmod(work_duration, 60)
    timer_label.config(text=f"{int(minutes):02}:{int(sec):02}")
    result_label.config(text="Timer reset. Press Start to begin again.")

def show_current_time():
    current_datetime = datetime.now().strftime("%H:%M")
    current_time.config(text=f"Time: {current_datetime}")
    root.after(1000, show_current_time)

show_current_time()
root.mainloop()