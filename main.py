from tkinter import *

window = Tk()     # Tk class for creating object window

window.minsize(width=400, height=300)  # minsize method
window.title("Convertor GUI Program")  # title method

my_label = Label(text="Enter the distance in Miles : ")
my_label.place(x=0, y=0)



input = Entry()
input_text = input.get()
input.place(x=201)

def button_clicked():
    

my_button = Button(text="Convert", command=button_clicked)
my_button.place(x=200, y=30)













window.mainloop()    # for holding window












