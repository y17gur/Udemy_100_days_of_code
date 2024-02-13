from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_MIN = 0.1
# SHORT_BREAK_MIN = 0.05
# LONG_BREAK_MIN = 0.15
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark = "✔ "
timer = ""
full_cycles = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text=f"00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_checkmark.config(text="")


def clic_reset():
    reset_timer()
    button_start.config(state="normal")
    global full_cycles
    full_cycles = 0
    label_full.config(text=f"Full cycles: {full_cycles}")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)
    button_start.config(state="disabled")
    if reps == 8:
        count_down(long_break_sec)
        label_timer.config(text="Long break", fg=GREEN)
    elif reps == 9:
        global full_cycles
        full_cycles += 1
        label_full.config(text=f"Full cycles: {full_cycles}")
        reset_timer()
        start_timer()
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="Short break", fg=PINK)
    else:
        count_down(work_sec)
        label_timer.config(text="Work", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        button_start.config(state="normal")
        start_timer()
        marks = ""
        work_session = reps // 2
        for _ in range(1, work_session + 1):
            marks += checkmark
        label_checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=60, bg=YELLOW)
window.resizable(width=False, height=False)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

# Labels
label_timer = Label(text="Timer", font=(FONT_NAME, 28, "bold"), bg=YELLOW, fg=GREEN)
label_timer.place(relx=0.5, rely=-0.2, anchor="n")  # Set anchor to the top center

label_checkmark = Label(text="", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
label_checkmark.place(relx=0.5, rely=1.1, anchor="center")

label_full = Label(text=f"Full cycles: {full_cycles}", font=(FONT_NAME, 11), bg=YELLOW, fg=RED)
label_full.place(relx=-0.15, rely=-0.28, anchor="n")  # Set anchor to the top center

# Buttons
button_start = Button(text="Start", width=5, height=1, command=start_timer)
button_start.place(relx=-0.15, rely=1.1, anchor="center")

button_reset = Button(text="Reset", width=5, height=1, command=clic_reset)
button_reset.place(relx=1.1, rely=1.1, anchor="center")

window.mainloop()
