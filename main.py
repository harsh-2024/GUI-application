# # def add(*args):
# #     sum = 0
# #     for n in args:
# #         sum+=n
# #     print(sum)
# #
# # add(2,4,6,8)
#
# def fun(**kwargs):
#     for key in kwargs:
#         print(key)
#
# fun(a=1, b=2, c=3)

from tkinter import *

window = Tk()     # Tk class for creating object window

window.minsize(width=600, height=500)  # minsize method
window.title("My First GUI Program")  # title method
my_label = Label(text="Graphical User Interface",font=("Arial", 24, "bold"))
my_label.pack(side="top")


def button_clicked():
    my_label.config(text="Button has clicked")   # pack method for representing it to the screen.


button = Button(text="Click Me", command=button_clicked)
button.pack(side="bottom")



window.mainloop()    # for holding window












