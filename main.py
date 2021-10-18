import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(text_timer, text="00:00")
    reps = 0
    check_marks.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    tick_count = math.floor(reps / 2)
    tick = "✔"
    check_marks.config(text=tick * tick_count)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps in [1, 3, 5, 7]:
        label_title.config(text="Work Time", fg=GREEN)
        count_down(work_sec)

    elif reps in [2, 4, 6]:
        label_title.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    elif reps == 8:
        label_title.config(text="Long Break", fg=RED)
        count_down(long_break_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(text_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
FONT = (FONT_NAME, 35, "bold")
text_timer = canvas.create_text(103, 138, text="00:00", font=FONT, fill="#F3F1F5")
canvas.grid(column=1, row=1)

label_title = Label(text='Timer', font=FONT, bg=YELLOW, fg=GREEN)
label_title.grid(column=1, row=0)

button_start = Button(text='Start', highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness=0, command= reset_timer)
button_reset.grid(column=2, row=2)

check_marks = Label(font=(FONT_NAME, 15, "bold"), highlightthickness=0, fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
