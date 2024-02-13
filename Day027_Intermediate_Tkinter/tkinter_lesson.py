# import tkinter
#
# window = tkinter.Tk()
# window.title("My First GUI")
# window.minsize(width=500, height=300)
#
# # Label
# my_label = tkinter.Label(text="A label 1", font=("Arial", 14, "bold"))
# my_label.pack()
#
# my_label["text"] = "A label 2"
# my_label.config(text="A label 3")
#
# from tkinter import *
#
#
# # def button_click():
# #     my_label.config(text="Clicked")
# #
# #
# # button = Button(text="Click", command=button_click)
# # button.pack()
#
# # Entry
# input_i = Entry(width=10)
# input_i.pack()
# input_i.get()
#
#
# def button_click():
#     my_label.config(text=input_i.get())
#     return
#
#
# button = Button(text=input_i.get(), command=button_click)
# button.pack()
# button.config(text="Click")

from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input_e.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input_e = Entry(width=10)
print(input_e.get())
input_e.grid(column=3, row=2)

window.mainloop()
