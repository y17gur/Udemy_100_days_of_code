from tkinter import *


def ml_to_km():
    miles = float(ml_input.get())
    km = round(miles * 1.609, 2)
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Ml to Km")
window.minsize(width=150, height=80)

ml_input = Entry(width=10)
ml_input.grid(column=1, row=0)

ml_label = Label(text="Miles")
ml_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal too")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=ml_to_km)
calc_button.grid(column=1, row=2)

window.mainloop()
